"""Validate local Markdown links and registry IDs from a full checkout."""
import json
from pathlib import Path
import re
import sys

root=Path(__file__).resolve().parents[1]
errors=[];count=0
for p in root.rglob('*.md'):
    if any(x in p.parts for x in ['.git','.venv','outputs']):continue
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if re.match(r'^[a-zA-Z]+:',target) or target.startswith('#'):continue
        path=target.split('#')[0]
        if path and not (p.parent/path).exists():errors.append(f'{p.relative_to(root)}: {target}')
        count+=1
registry=json.loads((root/'curriculum.json').read_text());ids=[x['id'] for x in registry['resources']]
if len(ids)!=len(set(ids)):errors.append('duplicate registry IDs')
for item in registry['resources']:
    for key in ['path','example','assignment','solutions','notes']:
        value=item.get(key)
        if isinstance(value,str) and not (root/value).exists():errors.append(f'{item["id"]}: missing {value}')
    for req in item.get('prerequisites',[]):
        if req not in ids:errors.append(f'{item["id"]}: unknown prerequisite {req}')
print(json.dumps({'internal_links':count,'resources':len(ids),'errors':errors},indent=2))
sys.exit(bool(errors))
