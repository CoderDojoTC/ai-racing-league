# Raspberry Pi Setup

## Install Conda for the ARM Processor

When asked:

*Do you wish the installer to prepend the Miniconda3 install location to PATH in your /root/.bashrc?*

Answer: yes

```sh
cd /tmp
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
chmod 755 Miniconda3-latest-Linux-armv7l.sh
./Miniconda3-latest-Linux-armv7l.sh
```

## Test Conda In Your PATH

```sh
which conda
```
Should return:

```
/home/pi/miniconda3/bin/conda
```

## Add the Raspberry Pi Channel to Conda
```sh
conda config --add channels rpi
conda install python=3.6
```

## Test Python
```sh
python --version
```

```
Python 3.6.6
```

## Create a DonkeyCar Conda Environment

```sh
conda create --name donkey python=3
```

```
The following NEW packages will be INSTALLED:

    ca-certificates: 2018.8.24-0          rpi
    certifi:         2018.8.24-py36_1     rpi
    ncurses:         6.1-h4f752ac_1       rpi
    openssl:         1.0.2r-hdff2a78_0    rpi
    pip:             18.0-py36_1          rpi
    python:          3.6.6-hd0568c0_1     rpi
    readline:        7.0-hcb560eb_1       rpi
    setuptools:      40.2.0-py36_0        rpi
    sqlite:          3.24.0-hfcb1bcf_1    rpi
    tk:              8.6.8-h849d6a0_0     rpi
    wheel:           0.31.1-py36_1        rpi
    xz:              5.2.4-hdff2a78_1     rpi
    zlib:            1.2.11-hdff2a78_1003 rpi

Proceed ([y]/n)? y
```

## Add the conda shell to the end of our .bashrc file

```sh
echo ". /home/pi/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
```

```sh
conda activate
```
The shell prompt should now be "base"

## Activate Your Donkey Python Environment

```sh
source activate donkey
```

You should see the prompt:

```
(donkey) pi@myhost:~ $
```

## Verify Git Is installed

```sh
git --version
```

git version 2.20.1

## Clone the DonkeyCar repository

```sh
git clone https://github.com/autorope/donkeycar
cd donkeycar
git checkout master
```

```sh
sudo apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev libgeos-dev git ntp
```

```sh
sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev libwebp-dev libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test
```

## Clone DonkeyCar Repo

```sh
pip freeze
```

certifi==2018.8.24


```sh
git clone https://github.com/autorope/donkeycar
cd donkeycar
pip install -e .[pi]

```

