# Install the NVIDIA Driver

Ideally you should be able to use the Ubuntu "Software and Updates" tool to install the NIVIDA driver.  This usually works, but if you get errors, you may need to use the unix shell.


## NVIDIA Card Verification
You can first verify that the GPU card has been installed and powered up.  We can use the "list hardware" command with the display option:

```sh
$ sudo lshw -C display
```

```
  *-display UNCLAIMED       
       description: VGA compatible controller
       product: GV102
       vendor: NVIDIA Corporation
       physical id: 0
       bus info: pci@0000:09:00.0
       version: a1
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress vga_controller bus_master cap_list
       configuration: latency=0
       resources: memory:f6000000-f6ffffff memory:e0000000-efffffff memory:f0000000-f1ffffff ioport:e000(size=128) memory:c0000-dffff
```

This shows that there is a GPU card installed but not claimed by the display.

## NVIDIA Devices
You can then use the ubuntu-drivers command to see the devices.

```sh
$ ubuntu-drivers devices
== /sys/devices/pci0000:00/0000:00:03.1/0000:09:00.0 ==
modalias : pci:v000010DEd00001E07sv000010DEsd000012A4bc03sc00i00
vendor   : NVIDIA Corporation
driver   : nvidia-driver-470 - distro non-free recommended
driver   : nvidia-driver-460-server - distro non-free
driver   : nvidia-driver-418-server - distro non-free
driver   : nvidia-driver-460 - distro non-free
driver   : nvidia-driver-450-server - distro non-free
driver   : xserver-xorg-video-nouveau - distro free builtin

== /sys/devices/pci0000:00/0000:00:01.2/0000:02:00.0/0000:03:04.0/0000:05:00.0 ==
modalias : pci:v00008086d00002723sv00008086sd00000084bc02sc80i00
vendor   : Intel Corporation
manual_install: True
driver   : backport-iwlwifi-dkms - distro free

```

## Ubuntu Drivers Autoinstall

```sh
sudo ubuntu-drivers autoinstall
```

This tool will tell you what drivers you need to install.

```sh
sudo apt-get install nvidia-driver-470
```

This will often generate errors but it will indicate what other libraries need to be installed for the 470 driver to work.

## Final Test

Now we are ready to probe the full GPU and get all the statistics of what is in the GPU.

```sh
nvidia-smi
```

```
Thu Jul 22 22:59:36 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.02    Driver Version: 470.57.02    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:09:00.0 Off |                  N/A |
| 41%   36C    P8     2W / 260W |    283MiB / 11016MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1327      G   /usr/lib/xorg/Xorg                 18MiB |
|    0   N/A  N/A      1398      G   /usr/bin/gnome-shell               71MiB |
|    0   N/A  N/A      1574      G   /usr/lib/xorg/Xorg                 98MiB |
|    0   N/A  N/A      1705      G   /usr/bin/gnome-shell               91MiB |
+-----------------------------------------------------------------------------+
```

If you don't get this or a similar display, you must continue to search for installation instructions.

After you get this screen you can reboot.

## CUDA Version

```sh
nvcc --version
```

Results:

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2017 NVIDIA Corporation
Built on Fri_Nov__3_21:07:56_CDT_2017
Cuda compilation tools, release 9.1, V9.1.85
```

### CUDA Tookkit Install for PyTorch

```sh
conda install cudatoolkit=<CUDA Version> -c pytorch
```

```sh
conda install cudatoolkit=11 -c pytorch
```