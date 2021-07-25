# Viewing Catalog Files

The data about each image, sometimes called the image "metadata" is stored in a file that ends with the extension .catalog.  If you open these files, you will see a simple layout that looks like the following:

```
{'_index': 16000, '_session_id': '21-07-20_0', '_timestamp_ms': 1626797545360, 'cam/image_array': '16000_cam_image_array_.jpg', 'user/angle': 1.0, 'user/mode': 'user', 'user/throttle': 0.5}
{'_index': 16001, '_session_id': '21-07-20_0', '_timestamp_ms': 1626797545411, 'cam/image_array': '16001_cam_image_array_.jpg', 'user/angle': 0.37, 'user/mode': 'user', 'user/throttle': 0.7}
{'_index': 16002, '_session_id': '21-07-20_0', '_timestamp_ms': 1626797545460, 'cam/image_array': '16002_cam_image_array_.jpg', 'user/angle': -0.23, 'user/mode': 'user', 'user/throttle': 0.25}
```

This file consists of multiple lines, each line starts and ends with curly braces "{" and "}".  Within these curly braces are a set of key-value pairs where the label is a string in single quotes followed by a colon, the value and a comma:

Here is that format with a the key and value on separate lines to make the line easier to read.

```json
{
    '_index': 16000,
    '_session_id': '21-07-20_0',
    '_timestamp_ms': 1626797545360,
    'cam/image_array':
    '16000_cam_image_array_.jpg',
    'user/angle': 1.0,
    'user/mode': 'user',
    'user/throttle': 0.5
}
```

This format is very similar to a JSON file with the following exceptions:

1. There is no root element to tell us when the JSON file starts and ends
2. There are no commas between the item

Here is what a properly formatted JSON file would look like:

```json
{
    "driveData": [
        {
            "_index": 16000,
            "_session_id": "21-07-20_0",
            "_timestamp_ms": 1626797545360,
            "cam/image_array": "16000_cam_image_array_.jpg",
            "user/angle": 1.0,
            "user/mode": "user",
            "user/throttle": 0.5
        },
        {
            "_index": 16001,
            "_session_id": "21-07-20_0",
            "_timestamp_ms": 1626797545411,
            "cam/image_array": "16001_cam_image_array_.jpg",
            "user/angle": 0.37,
            "user/mode": "user",
            "user/throttle": 0.70
        },
        {
            "_index": 16002,
            "_session_id": "21-07-20_0",
            "_timestamp_ms": 1626797545460,
            "cam/image_array": "16002_cam_image_array_.jpg",
            "user/angle": -0.23,
            "user/mode": "user",
            "user/throttle": 0.25
        }
    ]
}
```

Here is a sample JSON file reader that would read this file:

```py
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
```

Note that the open() function reads the file with the "r" option which indicates read-only mode.

## Converting Individual Catalog Lines to JSON
To read in the values of the catalog file we will open using a line-oriented data structure assuming that there is a newline at the end of each record.  We can then just the json library's ```loads()``` function which will convert each line to a JSON object.


Sample Objects.json file:

```
{"name":"Dan","age":19}
{"name":"Arun","age":20}
```

```py
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
    line_in_json = json.loads(line)
    count += 1
    print(count, ' ', end='')
    print(line_in_json)
    # the result is a Python dictionary
    print(line_in_json['name'])
    print("Name:", line_to_json["name"] )
    print("Age:", line_to_json["age"] )
```
