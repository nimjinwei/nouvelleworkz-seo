import json
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

# Load all 59 posts
with open('data/all_wp_posts_live.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Load GSC 28d data
try:
    with open('data/gsc_28d.json', 'r', encoding='utf-16') as f:
        gsc = json.load(f)
except Exception:
    with open('data/gsc_28d.json', 'r', encoding='utf-8') as f:
        gsc = json.load(f)

rows = gsc.get('rows', [])

# Map GSC by page URL
page_stats = defaultdict(lambda: {'imp': 0, 'clk': 0, 'queries': []})
for r in rows:
    p_norm = r['page'].rstrip('/') + '/'
    page_stats[p_norm]['imp'] += r['impressions']
    page_stats[p_norm]['clk'] += r['clicks']
    page_stats[p_norm]['queries'].append(r)

for p in posts:
    u = p['link'].rstrip('/') + '/'
    s = page_stats[u]
    p['imp'] = s['imp']
    p['clk'] = s['clk']
    p['top_queries'] = sorted(s['queries'], key=lambda x: x['impressions'], reverse=True)[:5]

# Group by thematic clusters
clusters = {
    "1. 商业工装与还原 (Commercial: Office, Retail, F&B, Reinstatement)": [],
    "2. BTO / 预购组屋指南 (BTO Timeline, Packages, Defects, Specific Estates)": [],
    "3. 二手房与老屋翻新 (Resale HDB Overhaul, 30-Year Flats, Structural/Permits)": [],
    "4. 公寓与有地住宅 (Condo MCST, Landed A&A, Ceiling/Lighting)": [],
    "5. 装修防坑与费用对比 (Cost Guides, ID vs Direct Contractor, VO Traps, Warranties)": [],
    "6. 空间专项：厨房与台面 (Kitchen, Cabinets, Sintered Stone vs Quartz)": [],
    "7. 空间专项：卫生间与防水 (Bathroom Makeover, Waterproofing, Balcony Tiling)": [],
    "8. 工种专项：木工定制 (Carpentry, Built-ins, Platform Beds, E0 Plywood)": [],
    "9. 工种专项：地面与地坪 (Flooring: Vinyl, SPC/LVT, Metallic Epoxy, Tiling)": [],
    "10. 工种专项：电工与智能家居 (Electrical Rewiring, DB Box, Smart Home)": [],
    "11. 工种专项：油漆与墙面 (Painting, Plastering, Skim Coat, Fluted Panels)": [],
    "12. 工种专项：敲墙与结构 (Hacking, Bomb Shelter, PE Endorsement)": [],
    "13. 其他 / 未归类": []
}

def get_cluster(p):
    t = p['title'].lower()
    slug = p['slug'].lower()
    
    # Commercial & Reinstatement
    if any(k in t or k in slug for k in ['reinstatement', 'f&b', 'f & b', 'restaurant', 'retail', 'salon', 'warehouse', 'office', 'commercial', 'fssd']):
        if 'flooring' in t or 'epoxy' in t or 'vinyl' in t:
            return "9. 工种专项：地面与地坪 (Flooring: Vinyl, SPC/LVT, Metallic Epoxy, Tiling)"
        return "1. 商业工装与还原 (Commercial: Office, Retail, F&B, Reinstatement)"
    
    # Resale
    if 'resale' in t or '30-year' in t or '30 year' in t:
        return "3. 二手房与老屋翻新 (Resale HDB Overhaul, 30-Year Flats, Structural/Permits)"
        
    # BTO
    if any(k in t or k in slug for k in ['bto', 'tengah']):
        return "2. BTO / 预购组屋指南 (BTO Timeline, Packages, Defects, Specific Estates)"
        
    # Condo & Landed
    if any(k in t or k in slug for k in ['condo', 'landed', 'l-box', 'ceiling']):
        return "4. 公寓与有地住宅 (Condo MCST, Landed A&A, Ceiling/Lighting)"
        
    # Cost, ID vs Contractor, VO, Warranty
    if any(k in t or k in slug for k in ['contractor', 'designer', 'vo', 'variation', 'warranty', 'deposit', 'luxury']):
        return "5. 装修防坑与费用对比 (Cost Guides, ID vs Direct Contractor, VO Traps, Warranties)"
        
    # Kitchen
    if any(k in t or k in slug for k in ['kitchen', 'sintered stone', 'quartz', 'countertop']):
        return "6. 空间专项：厨房与台面 (Kitchen, Cabinets, Sintered Stone vs Quartz)"
        
    # Bathroom
    if any(k in t or k in slug for k in ['bathroom', 'toilet', 'balcony', 'waterproofing', 'plumbing', 'grout']):
        return "7. 空间专项：卫生间与防水 (Bathroom Makeover, Waterproofing, Balcony Tiling)"
        
    # Carpentry
    if any(k in t or k in slug for k in ['carpentry', 'cabinet', 'tatami', 'platform bed', 'plywood', 'built-in']):
        return "8. 工种专项：木工定制 (Carpentry, Built-ins, Platform Beds, E0 Plywood)"
        
    # Flooring
    if any(k in t or k in slug for k in ['flooring', 'vinyl', 'epoxy', 'tile', 'tiling', 'porcelain']):
        return "9. 工种专项：地面与地坪 (Flooring: Vinyl, SPC/LVT, Metallic Epoxy, Tiling)"
        
    # Electrical
    if any(k in t or k in slug for k in ['rewiring', 'electrical', 'smart home']):
        return "10. 工种专项：电工与智能家居 (Electrical Rewiring, DB Box, Smart Home)"
        
    # Painting
    if any(k in t or k in slug for k in ['paint', 'painting', 'plaster', 'plastering', 'skim coat', 'panel']):
        return "11. 工种专项：油漆与墙面 (Painting, Plastering, Skim Coat, Fluted Panels)"
        
    # Hacking
    if any(k in t or k in slug for k in ['hacking', 'bomb shelter', 'pe endorsement']):
        return "12. 工种专项：敲墙与结构 (Hacking, Bomb Shelter, PE Endorsement)"
        
    return "13. 其他 / 未归类"

for p in posts:
    c = get_cluster(p)
    clusters[c].append(p)

print("="*60)
print(f"全站 Blog 文章总数: {len(posts)} 篇")
print("="*60)

for c_name, p_list in clusters.items():
    tot_imp = sum(x['imp'] for x in p_list)
    tot_clk = sum(x['clk'] for x in p_list)
    print(f"\n### {c_name} (共 {len(p_list)} 篇 | 28天展现: {tot_imp} | 点击: {tot_clk})")
    for x in sorted(p_list, key=lambda a: a['date'], reverse=True):
        tq = x['top_queries']
        tq_info = f" [Top Query: '{tq[0]['query']}' (Imp:{tq[0]['impressions']}, Pos:{tq[0]['position']:.1f})]" if tq else " [暂无独立GSC关键词]"
        print(f"  * [{x['date'][:10]}] {x['title']} (Imp:{x['imp']}, Clk:{x['clk']}){tq_info}")
