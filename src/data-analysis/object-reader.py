import os, json    
json_file = "objects.json"
script_dir = os.path.dirname(__file__)

# get a relative path to the script dir
path_to_catalog_file = script_dir + '/' + json_file

objects = json.load(open(path_to_catalog_file))

for person in objects:
    name = person['name']
    print(name)