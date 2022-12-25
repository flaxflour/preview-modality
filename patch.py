import json
import subprocess

with open('./dataloop.json') as json_file:
    data = json.load(json_file)
    prefix = data['version'][:-1]
    last_number = int(data['version'][-1])
    data['version'] = f'{prefix}{last_number + 1}'
    data['source']['tag'] = f'v{data["version"]}'
    current_version = data['source']['tag']
    print(current_version)
with open("./dataloop.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=2)

cmd = ['git', 'commit', '-am', current_version]
p = subprocess.Popen(cmd)
p.communicate()
cmd = ['git', 'tag', '-a', current_version, '-m', current_version]
p = subprocess.Popen(cmd)
p.communicate()