# Catalog Statistics

Now that we know how to reach each item in the tub catalog, we can now do some simple statistics on this data.  For example we can calculate the average throttle and steering angle and create some plots of the distribution of these values.

## Calculating Average Throttle and Angle

When we drive around the track each image records both the throttle and steering values at the instant the image was taken by the camera.  Although the values sent to the Electronic Speed Controller (ESC) and the servo are unique to every car, instead we store values that have been converted to a range between 0 and 1.  Both these values are [Normalized](#glossary#normalized) to values of between 0 and 1.

```py
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
```

returns:

```
100 items in dictionary
Average throttle:  0.31
Average angle: 0.53
```

These values look reasonable.  Our throttle should be between 0 and 1 and our average steering should be around 0.5.  If we drive in a pure circle only in a single direction the average angle will be offset from the 0.5 center value.

## Viewing Min and Max values

```py
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
min_throttle = 1
max_throttle = 0

total_angle = 0
min_angle = 1
max_angle = 0

# Add each line to our dictionary
for line in lines:
    # each line as a JSON dictionary object
    j = json.loads(line)
    count += 1
    dict.update(json.loads(line))
    total_throttle += j["user/throttle"]
    total_angle += j["user/angle"]

    # check for min and max throttle
    if j["user/throttle"] < min_throttle:
        min_throttle = j["user/throttle"]
    if j["user/throttle"] > max_throttle:
        max_throttle = j["user/throttle"]

    if j["user/angle"] < min_angle:
        min_angle = j["user/angle"]
    if j["user/angle"] > max_angle:
        max_angle = j["user/angle"]

print('\n')
print(count, "items in catalog")

print("Min throttle:", round(min_throttle, 3))
print("Average throttle: ", round(total_throttle/count, 3))
print("Max throttle:", round(max_throttle, 3))

print("Min angle:", round(min_throttle, 3))
print("Average angle:", round(total_angle/count, 3))
print("Max angle:", round(max_angle, 3))
print('\n')
```

returns:

```
100 items in catalog
Min throttle: -0.31
Average throttle:  0.308
Max throttle: 0.5
Min angle: -0.31
Average angle: 0.534
Max angle: 1.0
```

## Converting the Dictionary to a DataFrame

```py
df = pd.DataFrame(list(dict.items()))
print(df)
```

returns

```
                0                           1
0           _index                       16099
1      _session_id                  21-07-20_1
2    _timestamp_ms               1626797880229
3  cam/image_array  16099_cam_image_array_.jpg
4       user/angle                     0.56914
5        user/mode                        user
6    user/throttle                   0.0632649
```

## Plotting Steering Distributions


