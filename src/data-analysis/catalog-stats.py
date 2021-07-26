# program to read a DonkeyCar Catalog File
import os,json

# this program assumes that test.catalog is in the same directory as this script
# get the direcotry that this script is running
script_dir = os.path.dirname(__file__)

# get a relative path to the script dir
path_to_catalog_file = script_dir + '/test.catalog'

f = open(path_to_catalog_file)
lines = f.readlines()
# create a dictionary object
dict = {}
count = 0
total_throttle = 0
total_angle = 0
# Add each line to our dictionary
for line in lines:
    # each line as a JSON dictionary object
    j = json.loads(line)
    count += 1
    dict.update(json.loads(line))
    total_throttle += j["user/throttle"]
    total_angle += j["user/angle"]
print(count, "items in dictionary")
print("Average throttle: ", round(total_throttle/count, 3))
print("Average angle:", round(total_angle/count, 3))