import json, re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const DATA=(\{.+\});\s*\nconst CATEGORIES', content, re.DOTALL)
data = json.loads(m.group(1))

for p in data['problems']:
    if '接雨水' in p.get('title', ''):
        lines = p['desc'].split('\n')
        print(f"Total lines: {len(lines)}")
        for i, l in enumerate(lines):
            print(f"  [{i}] {repr(l[:120])}")
        break
