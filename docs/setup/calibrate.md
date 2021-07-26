# Calibrate

```sh
$ donkey calibrate --channel 0 --bus=1
```

Result

```
________             ______                   _________              
___  __ \_______________  /___________  __    __  ____/_____ ________
__  / / /  __ \_  __ \_  //_/  _ \_  / / /    _  /    _  __ `/_  ___/
_  /_/ // /_/ /  / / /  ,<  /  __/  /_/ /     / /___  / /_/ /_  /    
/_____/ \____//_/ /_//_/|_| \___/_\__, /      \____/  \__,_/ /_/     
                                 /____/                              

using donkey v4.2.1 ...
sombrero enabled
init PCA9685 on channel 0 address 0x40 bus 1
Using PWM freq: 60
Traceback (most recent call last):
  File "/home/pi/env/bin/donkey", line 33, in <module>
    sys.exit(load_entry_point('donkeycar', 'console_scripts', 'donkey')())
  File "/home/pi/projects/donkeycar/donkeycar/management/base.py", line 500, in execute_from_command_line
    c.run(args[2:])
  File "/home/pi/projects/donkeycar/donkeycar/management/base.py", line 219, in run
    c = PCA9685(channel, address=address, busnum=busnum, frequency=freq)
  File "/home/pi/projects/donkeycar/donkeycar/parts/actuator.py", line 30, in __init__
    self.pwm = Adafruit_PCA9685.PCA9685(address=address)
  File "/home/pi/env/lib/python3.7/site-packages/Adafruit_PCA9685/PCA9685.py", line 75, in __init__
    self.set_all_pwm(0, 0)
  File "/home/pi/env/lib/python3.7/site-packages/Adafruit_PCA9685/PCA9685.py", line 111, in set_all_pwm
    self._device.write8(ALL_LED_ON_L, on & 0xFF)
  File "/home/pi/env/lib/python3.7/site-packages/Adafruit_GPIO/I2C.py", line 114, in write8
    self._bus.write_byte_data(self._address, register, value)
  File "/home/pi/env/lib/python3.7/site-packages/Adafruit_PureIO/smbus.py", line 327, in write_byte_data
    self._device.write(data)
OSError: [Errno 121] Remote I/O error
sombrero disabled
```

## Diagnostics

### I2C Detect

```
i2cdetect -y 1
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

### I2C Device File

```
ls -ld /dev/i2*
crw-rw---- 1 root i2c 89, 1 Jul  3 13:17 /dev/i2c-1
```

### I2C Functions Enabled

```sh
 i2cdetect -F 1
```

returns:

```
Functionalities implemented by /dev/i2c-1:
I2C                              yes
SMBus Quick Command              yes
SMBus Send Byte                  yes
SMBus Receive Byte               yes
SMBus Write Byte                 yes
SMBus Read Byte                  yes
SMBus Write Word                 yes
SMBus Read Word                  yes
SMBus Process Call               yes
SMBus Block Write                yes
SMBus Block Read                 no
SMBus Block Process Call         no
SMBus PEC                        yes
I2C Block Write                  yes
I2C Block Read                   yes
```

Note that both SMBus Block Read and SMBus Block Process Call are set to no.  The rest are yes.

## Upgrade to Python 3.70

```sh
python3 -m virtualenv -p python3.7 env --system-site-packages
```

```
created virtual environment CPython3.7.3.final.0-32 in 2535ms
  creator CPython3Posix(dest=/home/pi/env, clear=False, no_vcs_ignore=False, global=True)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/pi/.local/share/virtualenv)
    added seed packages: pip==21.1.2, setuptools==57.0.0, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```

```sh
python --version
```

```
Python 3.7.3
```