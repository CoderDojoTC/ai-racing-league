# program to read a DonkeyCar Catalog File
import os,json

# this program assumes that test.json is in the same directory as this script
# get the direcotry that this script is running
script_dir = os.path.dirname(__file__)
# get a relative path to the script dir
path_to_catalog_file = script_dir + '/test.catalog'

# convert a string to a list of items
def iter_jsons(s):
    decoder = json.JSONDecoder()
    i = 0
    while True:
        doc, i2 = decoder.raw_decode(s[i:].strip())
        yield doc
        if i == i2:
            break
        i= i2

# Open the JSON test file for read only
f = open(path_to_catalog_file, 'r')
objects = json.load(f)

for item in objects:
    _index = item['_index']
    print(_index)