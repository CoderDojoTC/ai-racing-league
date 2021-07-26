# Community

Here are some sites that are of interest:


* [CoderDojo Twin Cities](http://coderdojotc.org) - where you can sign up to be a mentor or student
* [Twin Cities AI Racing League Meetup Site](https://www.meetup.com/Artificial-Intelligent-Racing-League/) - where we announce our public meetings

## DonkeyCar Hardware

* [DonkeyCar web site](http://donkeycar.com)
* [Donkey Car Nano Setup Page](https://docs.donkeycar.com/guide/robot_sbc/setup_jetson_nano/)
* [DonkeyCar Assembly Video](https://youtu.be/OaVqWiR2rS0) - Chris Anderson's detailed assembly video from 2018.

## Track Options

In Minnesota there is a place that sells used vinyl sign material.  For around $60 you can get a 16' X 25' used black billboard vinyl sign that is ideal for creating your own track.

![Used Black Vinyl Track for $60](img/track-vinyl-black.jpg)

[Billboard Tarps and Vinyl](https://billboardtarps.com/product-category/billboard-vinyl/) - We suggest you get a dark color (block or dark blue) and then tape down white edges and a yellow dashed line in the center.

![Sample Track Template](img/donkeycartrack4_1080x.jpg)

Sample of track.  Note the actual track is twice this size since it is still folded in half in this photo.

## Hardware Options

Raspberry Pi 3, 4, the Nvidia Nano, the Nvdia DX2, and the Intel Mobius Neural Stick
The base DonkeyCar today uses the Raspberry Pi 3+ which has a list price of $35.  This hardware is just barly able to process images in real-time.  Small changes in lighting will throw the car off the track.  The new Raspberry Pi 4 with 4GB RAM is a new option.

The Nvidia Nano on the other hand has 128 CUDA core processors and has more than enough power to drive around a track in real time with varied lighting conditions.  This is the hardware we have used for our first generation cars in the AI Racing League.

There are also college-level autonomous driving teams that use the more expensive Nvidia DX2 hardware.

## Nvidia Nano 
Jetson Nano References

* [Joseph Bastulli PyTorch Nano](https://github.com/bastulli/AutoCarJetsonNano)
* [Nvidia Jetson Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
* [Nvidia Jetson Nano Kaya Video](https://www.youtube.com/watch?v=X3qGDYie1_I)
* [Adding a Joystick to your DonkeyCar - From Dan McCreary's Blog](https://medium.com/@dmccreary/a-joystick-for-your-donkeycar-d4266c0b91f4)

## Videos

* [Video of Wide Track](https://www.youtube.com/watch?v=lfwq73D7oHg)
* [PID Theory and Steering](https://www.youtube.com/watch?v=4Y7zG48uHRo) - why using machine learning is easier than setting PID parameters.  This is covered in control theory.
* [Real time optimal control of an autonomous RC car with minimum-time maneuvers](https://www.youtube.com/watch?v=HADLEr5eTj0) - nice video of optimization of driving algorithm using a "U" shaped track.
* [Sparkfun Autonomous Vehicle Race from 2016](https://www.youtube.com/watch?v=NBr71Dww_-k)
* [Ed Murphy on Maker Faire](https://www.youtube.com/watch?v=cKhrV_RYVOw)
