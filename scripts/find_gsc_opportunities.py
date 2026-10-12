import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/gsc_28d.json', 'r', encoding='utf-16') as f:
    gsc = json.load(f)

rows = gsc.get('rows', [])

# 1. Queries landing on service pages with high impressions (Potential to create dedicated blog posts or support them)
service_page_queries = [r for r in rows if ('/residential/' in r['page'] or '/commercial/' in r['page']) and 'nouvelle' not in r['query'].lower()]
service_page_queries.sort(key=lambda x: x['impressions'], reverse=True)

print("=== TOP 25 HIGH-IMPRESSION QUERIES LANDING ON SERVICE PAGES ===")
for r in service_page_queries[:25]:
    p = r['page'].replace('https://nouvelleworkz.com', '')
    print(f"{r['query']:<45} | Imp: {r['impressions']:<4} | Clk: {r['clicks']:<2} | Pos: {r['position']:<4.1f} | Page: {p}")

# 2. Striking distance queries: Position between 5.0 and 20.0, Impressions >= 15
striking = [r for r in rows if 5.0 <= r['position'] <= 20.0 and r['impressions'] >= 15 and 'nouvelle' not in r['query'].lower()]
striking.sort(key=lambda x: x['impressions'], reverse=True)

print("\n=== TOP 25 STRIKING DISTANCE QUERIES (Pos 5-20, Imp >= 15) ===")
for r in striking[:25]:
    p = r['page'].replace('https://nouvelleworkz.com', '')
    print(f"{r['query']:<45} | Imp: {r['impressions']:<4} | Clk: {r['clicks']:<2} | Pos: {r['position']:<4.1f} | Page: {p}")

# 3. High Commercial Fit-Out & Office queries
comm_queries = [r for r in rows if any(k in r['query'].lower() for k in ['commercial', 'office', 'reinstatement', 'f&b', 'retail', 'restaurant']) and 'nouvelle' not in r['query'].lower()]
comm_queries.sort(key=lambda x: x['impressions'], reverse=True)

print("\n=== TOP 20 COMMERCIAL / B2B QUERIES ===")
for r in comm_queries[:20]:
    p = r['page'].replace('https://nouvelleworkz.com', '')
    print(f"{r['query']:<45} | Imp: {r['impressions']:<4} | Clk: {r['clicks']:<2} | Pos: {r['position']:<4.1f} | Page: {p}")
