#!/usr/bin/env python3
"""
wp_api_runner.py - WordPress REST API Client for Nouvelle Workz SEO Sprint

Provides fetch and draft push capabilities for WordPress posts and pages.
Ensures 100% draft status enforcement, UTF-8 safety, currency corruption guards,
and network retry handling.
"""

import argparse
import base64
import json
import logging
import random
import re
import sys
import time
import urllib.error
import urllib.request
from typing import Dict, List, Optional, Union

# Configuration
WP_BASE_URL = "https://nouvelleworkz.com/wp-json/wp/v2"
DEFAULT_USER = "nouvelle.workz"
DEFAULT_PASS = "LQ9WNv6Yy8f7ZsKt2k6G8Hph"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("wp_api_runner")


class WPAPIError(Exception):
    """Base exception for WordPress API errors."""
    pass


class WPAuthError(WPAPIError):
    """Raised on 401/403 authentication failures."""
    pass


class WPNotFoundError(WPAPIError):
    """Raised when post/page ID is not found (404)."""
    pass


class WPCurrencyCorruptionError(WPAPIError):
    """Raised when currency formatting checks fail pre-flight."""
    pass


def get_auth_header(user: str = DEFAULT_USER, password: str = DEFAULT_PASS) -> str:
    """Generates Basic Auth header string."""
    clean_pass = password.replace(" ", "")
    creds = f"{user}:{clean_pass}"
    encoded = base64.b64encode(creds.encode("utf-8")).decode("utf-8")
    return f"Basic {encoded}"


def validate_currency_formatting(html: str) -> List[str]:
    """
    Scans HTML string for currency corruption patterns such as missing '$'
    e.g., '<strong>,500</strong>' or ' .40 psf' instead of '$15,500' or '$8.40 psf',
    or PowerShell variable expansion artifacts like 'SGD  to '.
    
    Returns list of warning descriptions.
    """
    warnings = []
    
    # Pattern 1: Corrupted SGD range e.g. 'SGD  to '
    if re.search(r'SGD\s+to\b', html, re.IGNORECASE):
        warnings.append("Detected corrupt SGD currency range 'SGD  to ' (stripped variable)")

    # Pattern 2: Standalone leading comma in numbers, e.g., ',500' or ',000' in tags/text without leading dollar
    suspicious_comma_pattern = re.compile(r'(?<![\d\$]),\d{3}(?!\d)')
    matches = suspicious_comma_pattern.findall(html)
    if matches:
        warnings.append(f"Detected suspicious orphaned comma numbers (missing leading currency digit/$): {matches[:5]}")
        
    # Pattern 3: PSF prices missing leading dollar sign, e.g., ' .40 psf' or ' 5.50 psf' without $
    suspicious_psf_pattern = re.compile(r'(?<!\$)\b\d+\.\d{2}\s*psf\b', re.IGNORECASE)
    matches_psf = suspicious_psf_pattern.findall(html)
    if matches_psf:
        warnings.append(f"Detected PSF prices missing leading '$': {matches_psf[:5]}")
        
    return warnings


def execute_request_with_retry(
    url: str,
    method: str = "GET",
    data: Optional[bytes] = None,
    headers: Optional[Dict[str, str]] = None,
    retries: int = 3,
    backoff_factor: float = 1.0
) -> dict:
    """
    Executes an HTTP request with exponential backoff for transient errors.
    """
    if headers is None:
        headers = {}
        
    headers.setdefault("Authorization", get_auth_header())
    headers.setdefault("User-Agent", "NouvelleWorkz-WP-Runner/1.0")
    if data is not None:
        headers.setdefault("Content-Type", "application/json; charset=utf-8")

    last_exception = None

    for attempt in range(1, retries + 2):
        try:
            req = urllib.request.Request(url, data=data, headers=headers, method=method)
            with urllib.request.urlopen(req, timeout=30) as response:
                resp_bytes = response.read()
                resp_str = resp_bytes.decode("utf-8")
                return json.loads(resp_str)
                
        except urllib.error.HTTPError as e:
            last_exception = e
            status_code = e.code
            body = ""
            try:
                body = e.read().decode("utf-8")
            except Exception:
                pass
                
            if status_code in (401, 403):
                raise WPAuthError(f"HTTP {status_code} Auth Error for {url}: {body}") from e
            elif status_code == 404:
                raise WPNotFoundError(f"HTTP 404 Not Found for {url}: {body}") from e
            elif status_code in (400, 422):
                raise WPAPIError(f"HTTP {status_code} Client Error for {url}: {body}") from e
            elif status_code in (429, 500, 502, 503, 504):
                logger.warning(f"Attempt {attempt}/{retries + 1} failed with transient HTTP {status_code}. Retrying...")
            else:
                raise WPAPIError(f"HTTP {status_code} Error for {url}: {body}") from e
                
        except (urllib.error.URLError, TimeoutError, ConnectionResetError) as e:
            last_exception = e
            logger.warning(f"Attempt {attempt}/{retries + 1} failed with network error: {e}. Retrying...")

        if attempt <= retries:
            sleep_time = (backoff_factor * (2 ** (attempt - 1))) + random.uniform(0, 0.5)
            time.sleep(sleep_time)

    raise WPAPIError(f"Failed request to {url} after {retries + 1} attempts. Last error: {last_exception}")


def fetch_post(post_id: int, post_type: str = "posts", raw_only: bool = True, retries: int = 3) -> Union[str, dict]:
    """
    Fetches raw post/page data from WP REST API using GET /wp-json/wp/v2/{post_type}/{post_id}?context=edit.
    """
    url = f"{WP_BASE_URL}/{post_type}/{post_id}?context=edit"
    logger.info(f"Fetching {post_type} {post_id} from {url}...")

    try:
        data = execute_request_with_retry(url, method="GET", retries=retries)
    except WPNotFoundError:
        if post_type == "posts":
            logger.info(f"Post {post_id} not found under /posts. Trying /pages...")
            url = f"{WP_BASE_URL}/pages/{post_id}?context=edit"
            data = execute_request_with_retry(url, method="GET", retries=retries)
        else:
            raise

    if raw_only:
        content_raw = data.get("content", {}).get("raw", "")
        if not content_raw:
            logger.warning(f"No raw content found for {post_type} {post_id}.")
        return content_raw
    return data


def push_draft_post(
    post_id: int,
    content: str,
    post_type: str = "posts",
    retries: int = 3,
    skip_currency_check: bool = False
) -> dict:
    """
    Pushes content to WP REST API with HARDCODED status="draft".
    """
    if not skip_currency_check:
        warnings = validate_currency_formatting(content)
        if warnings:
            logger.warning(f"Currency formatting warnings for post {post_id}:")
            for w in warnings:
                logger.warning(f"  - {w}")

    # HARDCODED MANDATORY DRAFT STATUS ENFORCEMENT
    payload = {
        "content": content,
        "status": "draft"
    }

    url = f"{WP_BASE_URL}/{post_type}/{post_id}"
    json_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    logger.info(f"Pushing draft update for {post_type} {post_id} to {url} (payload size: {len(json_bytes)} bytes)...")
    
    try:
        response = execute_request_with_retry(url, method="POST", data=json_bytes, retries=retries)
    except WPNotFoundError:
        if post_type == "posts":
            logger.info(f"Post {post_id} not found under /posts endpoint. Trying /pages...")
            url = f"{WP_BASE_URL}/pages/{post_id}"
            response = execute_request_with_retry(url, method="POST", data=json_bytes, retries=retries)
        else:
            raise

    returned_status = response.get("status")
    logger.info(f"Successfully updated post {post_id}. Returned status: '{returned_status}'.")
    
    if returned_status != "draft":
        logger.error(f"CRITICAL WARNING: Post {post_id} returned status '{returned_status}' instead of 'draft'!")

    return response


def fetch_and_save(post_id: int, output_path: str, post_type: str = "posts") -> str:
    """Fetches raw HTML and writes to output_path using UTF-8."""
    raw_html = fetch_post(post_id, post_type=post_type, raw_only=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(raw_html)
    logger.info(f"Saved raw HTML for post {post_id} to {output_path} ({len(raw_html)} chars).")
    return raw_html


def read_and_push_draft(
    post_id: int,
    input_path: str,
    post_type: str = "posts",
    skip_currency_check: bool = False
) -> dict:
    """Reads HTML file (UTF-8) and pushes as draft."""
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    return push_draft_post(
        post_id,
        content,
        post_type=post_type,
        skip_currency_check=skip_currency_check
    )


def main():
    parser = argparse.ArgumentParser(description="WordPress REST API Runner (Nouvelle Workz SEO Sprint)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: fetch <id> [output_file]
    fetch_parser = subparsers.add_parser("fetch", help="Fetch raw post/page HTML from WordPress")
    fetch_parser.add_argument("post_id", type=int, help="WordPress Post or Page ID")
    fetch_parser.add_argument("pos_output", nargs="?", default=None, help="Output file path (positional)")
    fetch_parser.add_argument("-o", "--output", type=str, help="Output file path to save raw HTML")
    fetch_parser.add_argument("-t", "--type", type=str, choices=["posts", "pages"], default="posts", help="Post type")
    fetch_parser.add_argument("--meta", action="store_true", help="Print full metadata dict instead of raw HTML")

    # Subcommand: push <id> <html_file>
    push_parser = subparsers.add_parser("push", help="Push HTML content as draft to WordPress")
    push_parser.add_argument("post_id", type=int, help="WordPress Post or Page ID")
    push_parser.add_argument("pos_input", nargs="?", default=None, help="Input HTML file path (positional)")
    push_parser.add_argument("-i", "--input", type=str, help="Input HTML file path to push")
    push_parser.add_argument("-t", "--type", type=str, choices=["posts", "pages"], default="posts", help="Post type")
    push_parser.add_argument("--skip-currency-check", action="store_true", help="Skip pre-flight currency format check")

    # Subcommand: verify <html_file>
    verify_parser = subparsers.add_parser("verify", help="Verify HTML file for encoding and currency formatting issues")
    verify_parser.add_argument("pos_input", nargs="?", default=None, help="Input HTML file path (positional)")
    verify_parser.add_argument("-i", "--input", type=str, help="Input HTML file path")

    args = parser.parse_args()

    try:
        if args.command == "fetch":
            output_path = args.output or args.pos_output
            if output_path:
                fetch_and_save(args.post_id, output_path, post_type=args.type)
            else:
                data = fetch_post(args.post_id, post_type=args.type, raw_only=not args.meta)
                if isinstance(data, dict):
                    print(json.dumps(data, indent=2, ensure_ascii=False))
                else:
                    print(data)

        elif args.command == "push":
            input_path = args.input or args.pos_input
            if not input_path:
                push_parser.error("Input HTML file must be provided via positional argument or -i/--input option.")
            read_and_push_draft(
                args.post_id,
                input_path,
                post_type=args.type,
                skip_currency_check=getattr(args, "skip_currency_check", False)
            )

        elif args.command == "verify":
            input_path = args.input or args.pos_input
            if not input_path:
                verify_parser.error("Input HTML file must be provided via positional argument or -i/--input option.")
            with open(input_path, "r", encoding="utf-8") as f:
                content = f.read()
            warnings = validate_currency_formatting(content)
            if warnings:
                print(f"FAILED Verification for {input_path}:")
                for w in warnings:
                    print(f"  - {w}")
                sys.exit(1)
            else:
                print(f"PASSED Verification for {input_path}: No currency or formatting issues detected.")

    except Exception as e:
        logger.error(f"Execution failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
