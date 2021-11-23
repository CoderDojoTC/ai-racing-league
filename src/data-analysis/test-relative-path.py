import os,json
import pandas as pd
# program to read a DonkeyCar Catalog File


# this program assumes that test.catalog is in the same directory as this script
# get the direcotry that this script is running
script_dir = os.path.dirname(__file__)

# get a relative path to the script dir
path_to_catalog_file = script_dir + '/test.catalog'

print(path_to_catalog_file)