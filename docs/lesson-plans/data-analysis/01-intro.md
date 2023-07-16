# AI Racing League Data Analysis

## Why Analysis?

Data analysis is a core part of building accurate models that create high quality predictions.  Here are some sample analytics tasks:

1. Understand what data we have
2. Browse data sets
3. Run metrics that count the number of items in a dataset
4. Open sample items and view sample images
5. Look for groupings of data
6. Look at averages of values
7. Remove poor training data

## Tools: Python and Jupyter Notebooks

## Libraries: os, image, numpy, dataframes

```python
import os
from IPython.display import Image

image_dir = "/home/arl/mycar/data/dans-msp/data/images"

files = os.listdir(image_dir)
# last basement image is 1710
n = 1710
file_n = files[n]
file_2 = files[n+1]
print(n, file_n)
file_path1 = image_dir + '/' + file_n
file_path2 = image_dir + '/' + file_2
i1 = Image(file_path1)
i2 = Image(file_path2)
print(n+1, file_2)

display(i1, i2)
```