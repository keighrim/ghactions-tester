import json
import os

fullid = os.getenv('app_fullid')
shortid, version = fullid.rsplit('/', 1)

existing_data = json.load(open('docs/_data/apps.json'))
if shortid not in existing_data:
    existing_data[shortid] = []
existing_data[shortid].append(version)

with open('docs/_data/apps.json', 'w') as f:
    json.dump(existing_data, f, indent=2)
