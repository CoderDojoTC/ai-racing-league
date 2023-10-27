# Shell Commands for the GPU Server

The following is a list of shell commands for the AI Racing League GPU Server.  We have moved all the commands for setting up the NVIDIA GPU to the file [NVIDIA Driver Install](nvidia-driver-install.md).

The samples below are run if you are on the GPU running the Terminal shell or you have logged on using the secure shell program.

## Secure Shell Login

```linenums="0"
$ ssh arl@arl1.local
```

## Check the Version of Ubuntu

```sh
$ lsb_release -a
```

Response:

```
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.3 LTS
Release:	18.04
Codename:	bionic
```

## List the CPU Information

```sh
lscpu
```

Response:

```
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              12
On-line CPU(s) list: 0-11
Thread(s) per core:  2
Core(s) per socket:  6
Socket(s):           1
NUMA node(s):        1
Vendor ID:           AuthenticAMD
CPU family:          23
Model:               113
Model name:          AMD Ryzen 5 3600 6-Core Processor
Stepping:            0
CPU MHz:             2195.902
CPU max MHz:         3600.0000
CPU min MHz:         2200.0000
BogoMIPS:            7187.07
Virtualization:      AMD-V
L1d cache:           32K
L1i cache:           32K
L2 cache:            512K
L3 cache:            16384K
NUMA node0 CPU(s):   0-11
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate sme ssbd mba sev ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca
```

The key is that we have 12 CPUs and each CPU has two threads.  That means that we have 24 threads that run concurrent operations on this server.  This is plenty of capacity for our GPU server.

## RAM

```sh
free -m
```

Response:

```
              total        used        free      shared  buff/cache   available
Mem:          32124        1627       28879          75        1618       30019
Swap:          2047           0        2047
```

This indicates we have 32 GB RAM.  The GPU server should have a minimum of 8 GB of RAM.

## Disk Space

```sh
df -h /
```

Response:

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p3  229G  178G   40G  82% /
```

This shows we have a total of 229 gigabytes of RAM and we have 40 gigabytes available.  We will need about 4 GB for each training set we store.

### Per User Disk Usage

```sh
du -hs /home/* 2>/dev/null
```

Response:

```
8.5G	/home/arl
1.4G	/home/dan
16K	/home/dan2
155G	/home/donkey
```


### Add A New GPU Server User

```sh
adduser donkey
```
You can also allow the user to have "sudo" rights by using the following command:
```sh
sudo usermod -aG sudo donkey
```

### Change the Hostname

```sh
sudo vi /etc/hostname
```

Change the name to "gpu-server2" or a similar name.

## GPU Commands

### Display Type

```sh
sudo lshw -class display
```

Response:
```
       description: VGA compatible controller
       product: TU102 [GeForce RTX 2080 Ti Rev. A]
       vendor: NVIDIA Corporation
       physical id: 0
       bus info: pci@0000:09:00.0
       version: a1
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress vga_controller bus_master cap_list rom
       configuration: driver=nvidia latency=0
       resources: irq:101 memory:f6000000-f6ffffff memory:e0000000-efffffff memory:f0000000-f1ffffff ioport:e000(size=128) memory:c0000-dffff
```

Note that line 2 lists the product of TU102 [GeForce RTX 2080 Ti Rev. A] but it does not indicate how
much RAM we have on the defice.

### NVIDIA GPU Configuration

```sh
nvidia-smi
```

Result:
```
Mon Sep 25 14:17:46 2023       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.91.03    Driver Version: 460.91.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 208...  Off  | 00000000:09:00.0 Off |                  N/A |
| 40%   32C    P8    18W / 260W |    184MiB / 11018MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1026      G   /usr/lib/xorg/Xorg                 35MiB |
|    0   N/A  N/A      2315      G   /usr/lib/xorg/Xorg                 90MiB |
|    0   N/A  N/A      2509      G   /usr/bin/gnome-shell               10MiB |
|    0   N/A  N/A      4118      G   ...eLanguageDetectionEnabled       34MiB |
+-----------------------------------------------------------------------------+
```

This display is difficult to read.  But the key item is in the second column under the ```Memory-Usage``` area:

```184MiB / 11018MiB```

This says that we are using 184 megabytes and have 11.018 Gigabyte to use to run our machine learning tasks.

### NVIDIA GPU Monitor

The runs similar to the UNIX top command, but for the GPU.

```sh
watch -d -n 0.5 nvidia-smi
```

### NVIDIA GPU Utilization

This shows the GPU running at 42% utilization during the training process.

```
nvidia-smi
Mon Jul 26 20:24:16 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.02    Driver Version: 470.57.02    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:09:00.0  On |                  N/A |
| 41%   49C    P2   136W / 260W |  10892MiB / 11016MiB |     42%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1327      G   /usr/lib/xorg/Xorg                 18MiB |
|    0   N/A  N/A      1398      G   /usr/bin/gnome-shell               71MiB |
|    0   N/A  N/A      1574      G   /usr/lib/xorg/Xorg                155MiB |
|    0   N/A  N/A      1705      G   /usr/bin/gnome-shell               32MiB |
|    0   N/A  N/A     23722      G   ...AAAAAAAAA= --shared-files       25MiB |
|    0   N/A  N/A     27071      G   ...AAAAAAAAA= --shared-files        9MiB |
|    0   N/A  N/A     32486      C   ...a3/envs/donkey/bin/python    10571MiB |
+-----------------------------------------------------------------------------+
```
