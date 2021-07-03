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