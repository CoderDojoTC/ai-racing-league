# Docker on Nano

!!! Note
    These instructions were copied from a message on the Discord Server
    that were posed by user **naisy** on at 08/31/2023 5:48 AM.
    They are not supported by the DonkeyCar project (yet).

Due to the complexities of building the correct environments on the Nano, one alternative is to use the Docker container system.  Although this adds some additional overhead, it means that you can download a virtual machine with all the correct software installed.

You must have a minumum of a 64GB microSD card to run Docker on the NVIDIA Nano.

## Step 1: Download Docker GitHub Repo

In this step we will clone a repository that has some
very small UNIX shell scripts.

```sh
mkdir ~/projects
cd ~/projects
git clone https://github.com/naisy/Docker
cd Docker
```

## Step 2: Run the Permissions Shell Script

```
mkdir ~/docker
cp run-jetson-jp461-donkeycar??.sh ~/docker
cp run-jetson-jp461-gpio-permission.sh ~/docker

cd ~/docker
./run-jetson-jp461-gpio-permission.sh
```

## Step 3: Run the Main Shell Script

Due to memory limitations, only one of either DonkeyCar 4.5 or DonkeyCar 5.0 should be activated.

# DonkeyCar 4.5
./run-jetson-jp461-donkeycar45.sh

# or DonkeyCar 5.0
./run-jetson-jp461-donkeycar50.sh

## Login into the Virtual Machine

Log in to the jupyterlab terminal:
PC Web browser
for DonkeyCar 4.5

``
http://your_jetson_ip:8890/
```


for DonkeyCar 5.0 (dev3)

```
http://your_jetson_ip:8891/
Password: jupyterlab
Launch JupyterLab Terminal
```

DonkeyCar:
From this point on, it is exactly the same as a official donkeycar.
# create mycar
donkey createcar --path ~/data/mycar45
cd ~/data/mycar45
ls