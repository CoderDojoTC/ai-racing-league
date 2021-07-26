import os, json    
json_file = "objects.json"
script_dir = os.path.dirname(__file__)

# get a relative path to the script dir
path_to_catalog_file = script_dir + '/' + json_file

f = open(path_to_catalog_file)
lines = f.readlines()
 
count = 0
# Convert each line to a JSON object
for line in lines:
    line_to_json = json.loads(line)
    count += 1
    print(count, ' ', end='')
    print(line_to_json)
    print("Name:", line_to_json["name"] )
    print("Age:", line_to_json["age"] )
