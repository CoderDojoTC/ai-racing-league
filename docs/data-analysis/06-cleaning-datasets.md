# Cleaning Datasets

Up until now, we have only been viewing metrics and files.  These are all read-only operations. Now we will write our first programs that change the tub datasets.

## Splitting Datasets

In this lab we will assume that we want to break our data into two distinct subsets and place them in different "tubs", which are just directories that contain both the catalogs and images for a dataset.

You can begin by taking a single dataset in a tub and then duplicating that tub.  You can then selectively remove the data from the two tubs to effectively split the tubs.

The UNIX shell command to copy an entire directly is the "cp" command with the "-r" option for recursive copy.

```sh
cp -r from-dir to-dir
```

You can also add the "-v" option to see what files are being copied.

