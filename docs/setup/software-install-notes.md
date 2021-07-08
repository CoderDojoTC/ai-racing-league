# AI Racing League Software Installation

## Apt-get

Apt-get is the software package installed on the Raspberry Pi OS that allows you to install application libraries.

## DonkeyCar Libraries (required)
```sh
sudo apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev libgeos-dev git ntp
```

1. *build-essential* is the library that tracks software library dependency lists.
2. *python3* is the library that runs Python 3.  Note that the Raspberry Pi only has Python 2.7 as the default version.  All our DonkeyCar software requires Python 3.7.
3. *python3-dev* includes software development tools to manage python 3.
4. *python3-pip* is the pip tool that allows you to install a specific version of a python library
5. *python-virtualenv* is the tool that allows you to setup a virtual environment for the DonkeyCar specific libraries.  We use this tool instead of the conda tools.
6. *python3-numpy* are the numerical procssing python libraries.
7. *python3-picamera* are the libaries to work with the camera on the Raspberry pi.
8. *python3-pandas* are tools that allow data access for example reading CSV and JSON files.
9. *python2-rpi* are python libraries that work with the Raspberry Pi.
10. *i2ctools* are tools that allow you to work with the I2C communications bus.  This is the bus that is used to control the PWM board and which controls the throttle and steering.

The other libraries are mostly small support libraries used for supporting debugging.

## OpenCV (optional)
```sh
sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev libwebp-dev libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test
```

