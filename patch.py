import json

version = ''
data = dict()

with open('./dataloop.json') as json_file:
    data = json.load(json_file)
    prefix = data['version'][:-1]
    last_number = int(data['version'][-1])
    data['version'] = last_number + 1
with open("replayScript.json", "w") as jsonFile:
    json.dump(data, jsonFile)
