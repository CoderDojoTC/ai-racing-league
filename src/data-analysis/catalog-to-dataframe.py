import os,json
import pandas as pd
# program to read a DonkeyCar Catalog File


# this program assumes that test.catalog is in the same directory as this script
# get the direcotry that this script is running
script_dir = os.path.dirname(__file__)

# get a relative path to the script dir
path_to_catalog_file = script_dir + '/test.catalog'

print('data file path:', path_to_catalog_file)

f = open(path_to_catalog_file)
lines = f.readlines()
# create a dictionary object
records = []
count = 0
total_throttle = 0
total_angle = 0
# Add each line to our dictionary
for line in lines:
    # each line as a JSON dictionary object
    j = json.loads(line)
    count += 1
    records.append(j)

# print ('type:', type(dict))
# print('column count', len(dict))
# print('columns', dict.keys())

# df = pd.DataFrame(list(dict.items()), )
# df=pd.DataFrame.from_dict(dict, orient='index', columns={'id', 'session', 'time', 'img', 'angle', 'mode', 'throttle'})
df=pd.DataFrame(records)
# _index                                16099
# _session_id                      21-07-20_1
#_timestamp_ms                 1626797880229
#cam/image_array  16099_cam_image_array_.jpg
#user/angle                          0.56914
#user/mode                              user
#user/throttle                     0.0632649
# df.columns = ['id', 'session', 'timestamp', 'img', 'mode', 'angle', 'throttle']
df.rename({
    '_index': 'index', 
    'b_session_id': 'session',
    '_timestamp_ms': 'timestamp',
    'cam/image_array': 'img',
    'user/angle': 'angle', 
    'user/throttle': 'throttle'
    }, axis=1, inplace=True)

print(df)
print(df.describe())

df.to_csv("./test.csv")

'''
Create histogram of angle from dataframe
'''
import matplotlib.pyplot as plt

plt.hist(df['angle'], bins=20)
plt.savefig('./testAngle.png')

