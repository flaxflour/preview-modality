import shutil
import json
import os
 

with open('./dataloop.json') as json_file:
    data = json.load(json_file)
    panel_name = data['components']['panels'][0]['name']

print(f'Copying dist to panels/{panel_name}')
src_dir = 'dist'
dest_dir = f'panels/{panel_name}'
files = os.listdir(src_dir)
shutil.copytree(src_dir, dest_dir)