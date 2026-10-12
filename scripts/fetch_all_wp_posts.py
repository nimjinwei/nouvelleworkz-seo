import requests
import base64
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

user = 'nouvelle.workz'
pwd = 'LQ9W Nv6Y y8f7 ZsKt 2k6G 8Hph'.replace(' ', '')
token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
headers = {"Authorization": f"Basic {token}"}

all_posts = []
page = 1
while True:
    r = requests.get(f"https://nouvelleworkz.com/wp-json/wp/v2/posts?status=any&per_page=100&page={page}", headers=headers)
    if r.status_code != 200:
        break
    data = r.json()
    if not data:
        break
    all_posts.extend(data)
    page += 1

print(f"Total posts on website: {len(all_posts)}")
with open('data/all_wp_posts_live.json', 'w', encoding='utf-8') as f:
    json.dump([{
        'id': p['id'],
        'status': p['status'],
        'date': p['date'],
        'slug': p['slug'],
        'title': p['title']['rendered'],
        'link': p['link'],
        'categories': p['categories']
    } for p in all_posts], f, indent=2, ensure_ascii=False)

print("Saved to data/all_wp_posts_live.json")
