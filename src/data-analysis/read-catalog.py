# program to read a DonkeyCar Catalog File
import os,json

# this program assumes that test.catalog is in the same directory as this script
# get the direcotry that this script is running
script_dir = os.path.dirname(__file__)

# get a relative path to the script dir
path_to_catalog_file = script_dir + '/test.catalog'

f = open(path_to_catalog_file)
lines = f.readlines()
 
count = 0
# Convert each line to a JSON object
for line in lines:
    # each line as a JSON dictionary object
    j = json.loads(line)
    count += 1
    print('\n\nline:', count)
    # print(j)
    print("Index:", j["_index"] )
    print("Session:", j["_session_id"] )
    print("Timestamp:", j["_timestamp_ms"] )
    print("cam/image_array:", j["cam/image_array"] )
    print("user/angle:", j["user/angle"] )
    print("user/mode:", j["user/mode"] )
    print("user/throttle:", j["user/throttle"] )
