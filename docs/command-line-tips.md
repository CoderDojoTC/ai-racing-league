# Command Line Tips

## Get Setup

```sh
git config --global user.name "Joe Smith"
git config --global user.email "Joe.Smith123@gmail.com"
git config --global credential.helper store
```

## Raspberry Pi Command Line Tips

From Terminal, you can open the current directory in the File Manager using the ```xdg-open``` command.  This is similar to the Mac open command.

```sh
$ xdg-open .
```
## See If the PWM Board Is Working

```sh
i2cdetect -l
```

This should return
```
i2c-1	i2c   bcm2835 (i2c@7e804000)   I2C adapter
```

```sh
i2cdetect -y 1
```

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --                         
```

Note that the line 40 and 70 has values under column 0 (I2C bus 1)
If you unplug the data you should get:

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --                        
```

## SD Card Speed Test

Home -> Accessories -> Raspberry Pi Diagnostics

```
Raspberry Pi Diagnostics - version 0.9
Sat Jul  3 14:25:23 2021

Test : SD Card Speed Test
Run 1
prepare-file;0;0;20628;40
seq-write;0;0;21999;42
rand-4k-write;0;0;4498;1124
rand-4k-read;8695;2173;0;0
Sequential write speed 21999 KB/sec (target 10000) - PASS
Random write speed 1124 IOPS (target 500) - PASS
Random read speed 2173 IOPS (target 1500) - PASS
Test PASS
```