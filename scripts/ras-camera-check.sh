#!/bin/sh
# Open a small window that shows a video of the camera
# preview parameters are x, y, width and height
raspivid -t 10000 --preview 100,100,400,200
