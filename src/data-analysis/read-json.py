# program to read a DonkeyCar Catalog File
import os,json

# this program assumes that test.json is in the same directory as this script
# get the direcotry that this script is running
script_dir = os.path.dirname(__file__)
# get a relative path to the script dir
path_to_json_file = script_dir + '/test.json'

# Open the JSON test file for read only
f = open(path_to_json_file, 'r')
  
# returns JSON object as a dictionary
data = json.load(f)
  
# Iterating through the json file for the items in the drive data dictionary
for i in data['driveData']:
    print(i)
  
# Close the JSON file
f.close()