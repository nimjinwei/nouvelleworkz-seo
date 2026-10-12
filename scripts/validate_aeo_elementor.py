#!/usr/bin/env python3
"""
validate_aeo_elementor.py — Automated AEO & Elementor Quality Assurance Validator

Validates upgraded WordPress page HTML payloads against Elementor layout rules,
definition sentence length bounds, meta-phrase exclusion, semantic numerical tables,
PowerShell currency variable corruption, and FAQPage JSON-LD schema standards.

Author: NouvelleWorkz Team
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set
from bs4 import BeautifulSoup

# --- DATA STRUCTURES ---

@dataclass
class CheckResult:
    passed: bool
    name: str
    message: str
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ValidationResult:
    overall_passed: bool
    elementor_data_ids_preserved: CheckResult
    definition_sentence_present: CheckResult
    meta_phrases_prohibited: CheckResult
    tables_present: CheckResult
    json_ld_valid: CheckResult
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "overall_passed": self.overall_passed,
            "checks": {
                "elementor_data_ids_preserved": {
                    "passed": self.elementor_data_ids_preserved.passed,
                    "message": self.elementor_data_ids_preserved.message,
                    "details": self.elementor_data_ids_preserved.details
                },
                "definition_sentence_present": {
                    "passed": self.definition_sentence_present.passed,
                    "message": self.definition_sentence_present.message,
                    "details": self.definition_sentence_present.details
                },
                "meta_phrases_prohibited": {
                    "passed": self.meta_phrases_prohibited.passed,
                    "message": self.meta_phrases_prohibited.message,
                    "details": self.meta_phrases_prohibited.details
                },
                "tables_present": {
                    "passed": self.tables_present.passed,
                    "message": self.tables_present.message,
                    "details": self.tables_present.details
                },
                "json_ld_valid": {
                    "passed": self.json_ld_valid.passed,
                    "message": self.json_ld_valid.message,
                    "details": self.json_ld_valid.details
                }
            },
            "errors": self.errors,
            "warnings": self.warnings
        }


# --- VALIDATION SUBSYSTEMS ---

def check_elementor_preservation(orig_soup: Optional[BeautifulSoup], mod_soup: BeautifulSoup) -> CheckResult:
    if orig_soup is None:
        return CheckResult(
            passed=True,
            name="Elementor Layout Preservation",
            message="Skipped data-id comparison (no original HTML provided)",
            details={"skipped": True}
        )
    
    orig_ids = {tag['data-id'] for tag in orig_soup.find_all(True, attrs={'data-id': True})}
    mod_ids = {tag['data-id'] for tag in mod_soup.find_all(True, attrs={'data-id': True})}
    
    missing_ids = orig_ids - mod_ids
    
    wrapper_classes = ['elementor-section', 'elementor-column', 'elementor-widget', 'elementor-widget-container']
    orig_wrappers = sum(len(orig_soup.find_all(class_=cls)) for cls in wrapper_classes)
    mod_wrappers = sum(len(mod_soup.find_all(class_=cls)) for cls in wrapper_classes)
    
    passed = (len(missing_ids) == 0) and (mod_wrappers >= orig_wrappers)
    
    msg = f"100% Elementor data-id attributes and wrappers preserved ({len(orig_ids)} matched)." if passed else \
          f"Elementor DOM corruption detected: {len(missing_ids)} missing data-id attribute(s)."
          
    return CheckResult(
        passed=passed,
        name="Elementor Layout Preservation",
        message=msg,
        details={
            "original_id_count": len(orig_ids),
            "modified_id_count": len(mod_ids),
            "missing_ids": sorted(list(missing_ids)),
            "original_wrapper_count": orig_wrappers,
            "modified_wrapper_count": mod_wrappers
        }
    )


def check_definition_sentence(mod_soup: BeautifulSoup) -> CheckResult:
    paragraphs = mod_soup.find_all('p')[:6]
    candidates = []
    best_match = None
    
    for idx, p in enumerate(paragraphs):
        text = p.get_text(strip=True)
        if not text:
            continue
            
        words = re.findall(r'\b[\w\'-]+\b', text)
        wc = len(words)
        candidates.append({"index": idx, "word_count": wc, "snippet": text[:80] + "..."})
        
        if 40 <= wc <= 60:
            best_match = {"index": idx, "word_count": wc, "text": text}
            break
            
    passed = best_match is not None
    msg = f"Valid definition sentence found at paragraph #{best_match['index']} ({best_match['word_count']} words)." if passed else \
          "No 40-60 word definition sentence found near top of post."
          
    return CheckResult(
        passed=passed,
        name="Definition Sentence Check",
        message=msg,
        details={"matched_paragraph": best_match, "candidates_checked": candidates}
    )


def check_meta_phrases(html_content: str) -> CheckResult:
    forbidden_re = re.compile(
        r'(IMPORTANT\s+DIRECT\s+ANSWER|AEO\s+DIRECT\s+ANSWER|Direct\s+Answer\s+for\s+AI|AEO\s+Definition|In\s+this\s+section\s+we\s+define|Below\s+is\s+a\s+definition\s+of)',
        re.IGNORECASE
    )
    
    matches = []
    lines = html_content.splitlines()
    for line_no, line in enumerate(lines, 1):
        for match in forbidden_re.finditer(line):
            matches.append({
                "line": line_no,
                "matched_text": match.group(0),
                "context": line.strip()[:100]
            })
            
    passed = len(matches) == 0
    msg = "Zero forbidden meta-phrases detected." if passed else \
          f"Meta-phrase prohibition failed: {len(matches)} forbidden string match(es) found."
          
    return CheckResult(
        passed=passed,
        name="Meta-Phrase Exclusion Scanner",
        message=msg,
        details={"matches": matches}
    )


def check_tables_and_currency(html_content: str, mod_soup: BeautifulSoup) -> CheckResult:
    errors = []
    
    # PowerShell currency corruption check
    corrupt_patterns = [
        (r'SGD\s+to\b', "Corrupt currency string 'SGD  to ' detected"),
        (r'(?<![\d\$]),\d{3}(?!\d)', "Corrupt thousand figure missing leading currency digit/$ detected"),
        (r'(?<![\d\$])\.\d{2}\s*psf\b', "Corrupt psf rate '.40 psf' detected (missing leading dollar digit)"),
        (r'(?<!\$)\b\d+\.\d{2}\s*psf\b', "Corrupt psf rate missing leading '$' detected")
    ]
    for pattern, err_msg in corrupt_patterns:
        if re.search(pattern, html_content, re.IGNORECASE):
            errors.append(f"PowerShell Currency Trap: {err_msg}")
            
    has_numerical_data = bool(re.search(r'(\$\d+|\d+\s*psf|SGD\s*\$\d+)', html_content))
    tables = mod_soup.find_all('table')
    table_details = []
    
    if has_numerical_data and not tables:
        errors.append("Numerical/pricing data detected, but zero <table> elements found.")
    else:
        for idx, table in enumerate(tables):
            has_thead = bool(table.find('thead'))
            has_th = bool(table.find_all('th'))
            has_tbody = bool(table.find('tbody'))
            has_td = bool(table.find_all('td'))
            
            valid = has_thead and has_th and has_tbody and has_td
            table_details.append({
                "table_index": idx,
                "valid": valid,
                "has_thead": has_thead,
                "has_th": has_th,
                "has_tbody": has_tbody,
                "has_td": has_td
            })
            if not valid:
                errors.append(f"Table #{idx} missing mandatory semantic HTML tags (<thead>, <th>, <tbody>, <td>).")
                
    passed = len(errors) == 0
    msg = f"Semantic tables valid ({len(tables)} table(s) checked), 0 currency corruptions." if passed else \
          f"Table/Currency validation failed: {'; '.join(errors)}"
          
    return CheckResult(
        passed=passed,
        name="Numerical Tables & Currency Check",
        message=msg,
        details={"table_count": len(tables), "errors": errors, "tables": table_details}
    )


def check_faq_json_ld(mod_soup: BeautifulSoup) -> CheckResult:
    scripts = mod_soup.find_all('script', type='application/ld+json')
    faq_objects = []
    syntax_errors = []
    
    for idx, script in enumerate(scripts):
        raw_text = script.string or script.get_text()
        if not raw_text or not raw_text.strip():
            continue
            
        try:
            data = json.loads(raw_text)
            candidates = []
            if isinstance(data, dict):
                if data.get('@type') == 'FAQPage':
                    candidates.append(data)
                elif '@graph' in data and isinstance(data['@graph'], list):
                    for item in data['@graph']:
                        if isinstance(item, dict) and item.get('@type') == 'FAQPage':
                            candidates.append(item)
                            
            for faq in candidates:
                main_entity = faq.get('mainEntity', [])
                if not isinstance(main_entity, list):
                    continue
                    
                valid_qa_count = 0
                qa_details = []
                for qa in main_entity:
                    if isinstance(qa, dict) and qa.get('@type') == 'Question':
                        q_name = qa.get('name', '')
                        ans = qa.get('acceptedAnswer', {})
                        ans_type = ans.get('@type') if isinstance(ans, dict) else None
                        ans_text = ans.get('text', '') if isinstance(ans, dict) else ''
                        
                        if q_name and ans_type == 'Answer' and ans_text:
                            valid_qa_count += 1
                            qa_details.append({"question": q_name[:60], "answer_len": len(ans_text)})
                            
                faq_objects.append({
                    "script_index": idx,
                    "question_count": valid_qa_count,
                    "qa_details": qa_details
                })
        except Exception as e:
            syntax_errors.append(f"Script #{idx} JSON parse error: {str(e)}")
            
    valid_faq = any(f["question_count"] >= 3 for f in faq_objects)
    passed = valid_faq and len(syntax_errors) == 0
    
    if passed:
        msg = f"Valid FAQPage JSON-LD schema found with {faq_objects[0]['question_count']} Q&A items."
    else:
        msg = "FAQPage JSON-LD check failed (missing valid FAQPage, < 3 Q&As, or invalid JSON syntax)."
        
    return CheckResult(
        passed=passed,
        name="FAQPage JSON-LD Schema Validator",
        message=msg,
        details={"faq_objects": faq_objects, "syntax_errors": syntax_errors}
    )


# --- MAIN ENTRY POINT ---

def validate_html(original_html: Optional[str], modified_html: str) -> ValidationResult:
    orig_soup = BeautifulSoup(original_html, 'html.parser') if original_html else None
    mod_soup = BeautifulSoup(modified_html, 'html.parser')
    
    res_elem = check_elementor_preservation(orig_soup, mod_soup)
    res_def = check_definition_sentence(mod_soup)
    res_meta = check_meta_phrases(modified_html)
    res_tab = check_tables_and_currency(modified_html, mod_soup)
    res_faq = check_faq_json_ld(mod_soup)
    
    all_checks = [res_elem, res_def, res_meta, res_tab, res_faq]
    overall_passed = all(c.passed for c in all_checks)
    
    errors = [f"{c.name}: {c.message}" for c in all_checks if not c.passed]
    
    return ValidationResult(
        overall_passed=overall_passed,
        elementor_data_ids_preserved=res_elem,
        definition_sentence_present=res_def,
        meta_phrases_prohibited=res_meta,
        tables_present=res_tab,
        json_ld_valid=res_faq,
        errors=errors
    )


def main():
    parser = argparse.ArgumentParser(description="AEO & Elementor Validator Engine")
    parser.add_argument("--original", help="Path to original raw HTML file", default=None)
    parser.add_argument("--modified", help="Path to modified upgraded HTML file", required=True)
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    parser.add_argument("--verbose", action="store_true", help="Display verbose diagnostics")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.modified):
        print(f"Error: Modified file not found at '{args.modified}'", file=sys.stderr)
        sys.exit(2)
        
    orig_content = None
    if args.original:
        if not os.path.exists(args.original):
            print(f"Error: Original file not found at '{args.original}'", file=sys.stderr)
            sys.exit(2)
        with open(args.original, 'r', encoding='utf-8', errors='ignore') as f:
            orig_content = f.read()
            
    with open(args.modified, 'r', encoding='utf-8', errors='ignore') as f:
        mod_content = f.read()
        
    result = validate_html(orig_content, mod_content)
    
    if args.json:
        print(json.dumps(result.to_dict(), indent=2))
    else:
        print("=" * 80)
        print("AEO & ELEMENTOR VALIDATION REPORT")
        print("=" * 80)
        print(f"Modified File: {args.modified}")
        print(f"Original File: {args.original or 'None'}")
        print("-" * 80)
        
        checks = [
            result.elementor_data_ids_preserved,
            result.definition_sentence_present,
            result.meta_phrases_prohibited,
            result.tables_present,
            result.json_ld_valid
        ]
        
        for c in checks:
            status = "[PASS]" if c.passed else "[FAIL]"
            print(f"{status} {c.name}: {c.message}")
            if args.verbose and c.details:
                print(f"       Details: {c.details}")
                
        print("-" * 80)
        passed_count = sum(1 for c in checks if c.passed)
        if result.overall_passed:
            print(f"OVERALL STATUS: PASSED ({passed_count}/{len(checks)} Checks Passed)")
        else:
            print(f"OVERALL STATUS: FAILED ({len(result.errors)} Check(s) Failed)")
        print("=" * 80)
        
    sys.exit(0 if result.overall_passed else 1)


if __name__ == "__main__":
    main()
