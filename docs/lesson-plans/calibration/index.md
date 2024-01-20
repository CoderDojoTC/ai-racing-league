# Donkey Car Calibration

We will be following the same steps
outlined in the [Donkey Car Docs](https://docs.donkeycar.com/guide/calibrate/)

To run calibration, connect a HDMI connector to the Pi and then boot.  You will also need a keyboard and mouse
and a charged 7.2-volt battery for calibration.

We would like students to work in pairs
to calibrate each car and record the
configuration parameters in a Python
configuration file.  Some of the cars are in
a plastic bin and these bins sometimes have
a card with the right configuration parameters on them.

Our cars all use the PCA9685 I2C to PWM chip.
We don't have the Donkey Car Hats.

Make sure the power LED on the PCA9685 is on.
If not, check the power and ground connections
to the Raspberry Pi SBC 40-pin connector.

!!! Note
    Some of the sample configuration files use an older format.  Make sure you ONLY modify the configuration files that are generated with the
    command that generates the ```mycar``` files.

## Calibration Command

There is an on/off switch on the Electronic Speed Control.  Make sure it is in the ON position and
that the motor battery is charged and connected.

When you turn the switch on you MUST hear the confirmation beep.  If you don't hear it you
need to check the battery and connections.

```sh
donkey calibrate --channel <your_steering_channel> --bus=<your_i2c_bus>
```

By default, our cars use channel 0 for the throttle and channel 1 for the steering.  If the team that
assembled the car switched the connections on the PWM card these may be reversed.


The key parameters to record are:

**Throttle:**

1. Max forward speed: THROTTLE_FORWARD_PWM
2. Neutral: THROTTLE_STOPPED_PWM
3. Max reverse speed: THROTTLE_REVERSE_PWM

**Steering**

1. Max left turn: STEERING_LEFT_PWM 
2. Max right turn: STEERING_RIGHT_PWM 

These should be placed online in a file that
is associated with each car name or number.

## Challenges Setting Reverse

Reverse on RC cars is a little tricky because the ESC must receive the following sequence:

1. a reverse pulse
2. a zero pulse
3. a reverse pulse to start to go backwards. 

To calibrate a reverse PWM setting...

Use the same technique as above 

1. Set the PWM setting to your zero throttle.
2. Enter the reverse value, then the zero throttle value, then the reverse value again.
3. Enter values +/- 10 of the reverse value to find a reasonable reverse speed. Remember this reverse PWM value.

Here is the basic command to edit the config file:

```sh
nano ~/mycar/myconfig.py
```
The Raspberry Pi's also have Python IDEs installed so you can also use those editors.

* [Sample V1 Configuration File](https://github.com/CoderDojoTC/ai-racing-league/blob/master/configs/dk4-config.py)
