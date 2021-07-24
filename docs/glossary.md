# AI Racing League Glossary of Term

#### Calibration
A step in setting up a DonkeyCar where around five values configuration file is created that reflect the physical aspects of the RC car.  There are three parameters for the throttle and two parameters for the steering.  It is important to get these five parameters correct so you can precisely drive your DonkeyCar.

#### CoderDojo
An international program of over 2,300 coding clubs that uses data-driven practices to get students interested in coding.  Many of the aspects of the AI Racing League uses these same principals.

Key aspects of CoderDojo are:

* No fees for events - accessible to all
* Mentor ratios of no more than three students per mentor
* Project-based learning
* Focus on getting students to work in teams (social learning)
* Student-directed projects
* Focus on programs for girls in coding and underprivileged youth

Their main web site is: [http://coderdojo.com/](http://coderdojo.com/)

#### CoderDojo Twin Cities Python Labs

These labs are a set of free-courses to learn Python using fun turtle graphics.  There is no experience needed.

* [Link to CoderDojo Twin Cities Python Labs](http://coderdojotc.com/python)


#### CoderDojo Twin Cities MicroPython Labs

These labs are a set of free-courses to learn MicroPython.  You should have a
background in Python to use these labs.  There are lessons in sensors, motors and robots.

* [Link to CoderDojo Twin Cities MicroPython Labs](http://coderdojotc.com/micropython)

#### CoderDojo Base MicroPython Robot

This is a $25 robot that you build and program with MicroPython.  If you are working on a project that will lead up to a full DonkeyCar, this is an ideal project to get you started.
The robot will get you familiar with concepts like PWM, motor controllers and sensors.

* [Blog article](https://dmccreary.medium.com/raspberry-pi-pico-robot-in-micropython-51f956486270)
* [Microsite Raspberry Pi Pico MicroPython Base Robot](https://www.coderdojotc.org/micropython/robots/02-base-bot/)

#### Code Savvy
Code Savvy is a not-for-profit organization with 501(c)3 status from the IRS that the AI Racing League works as a sub-project.  All the AI Racing League financials are organized under a Code Savvy program.  Donations to the AI Racing League should be done though Code Savvy donations.  Questions about Code Savvy can be sent to kidscode@codesavvy.org

* [Code Savvy Web Site](http://codesavvy.org)

#### Concept Cards
These are small laminated cards that have concepts information on them that students can learn.  The idea is one-concept per card.  See the [CoderDojo TC Guide for Authoring Concept Cards](https://www.coderdojotc.org/CoderDojoTC/designing-concept-cards/)

#### Donkey Car
This is a trademarked name of a car that is used at our events.  The name implies "ugly" so you know that they are not designed to look pretty, just functional cars with a camera on the front.

* [DonkeyCar web site](http://donkeycar.com)

#### GPU Server

![GPU Case with Handle](GPU-case-with-handle.png)

Each of the AI Racing League events usually has at least one GPU server for training our models.  These are typically small portable PCs with a GPU card in them.  The entire GPU server cost around $1,200 each and can train a 20,000 image data set in under five minutes.

We typically suggest that clubs writing grants use a [NVIDIA RTX 2070](https://www.nvidia.com/en-us/geforce/graphics-cards/rtx-2070/) or similar card since it is both fast enough for 10-team events but cost effective that schools can afford them.

Note that we have tried to use cloud-based services at some of our events but we can't be guaranteed that there is enough WiFi bandwidth to move large datasets and models to and from the cloud.  We feel that the tasks involved in setting up the GPU server is also a valuable skill for our students.

* See the [GPU Parts List](admin/gpu-parts.md) for a list of components.

#### Electronic Speed Control
An electronic circuit that controls and regulates the speed of an electric motor. It also can reverse the direction of the motor.  Our ESC

* [Wikipedia Page on Electronic Speed Control](https://en.wikipedia.org/wiki/Electronic_speed_control)

#### Fifteen Degree Camera Angle
The angle our cameras need to point down to have a good view of the road ahead.

#### Pulse Width Modulation
The way that we control the [Electronic Speed Controller] (ESC) and the servo by sending digital square waves with a variable ratio of the width of the positive part of the square wave.

* [Wikipeda Page on Pulse-width modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation)

#### Tracks

We want our clubs to all have affordable but high-quality tracks that are easy to roll up and store.  Our suggestion is to find used billboard vinyl in a dark color (black or dark blue) and then use white and yellow tape to place down the lines.


* https://billboardtarps.com/product-category/billboard-vinyl/
* [YouTube Video](https://youtu.be/urOLMJDGVdw)

#### Training Step
The step in DonkeyCar setup where we take approximately 20,000 small image files and the throttle and steering information with each image to build a deep neural network.  The training step requires us to move the data off the DonkeyCar's SD card and transfer the data to a more powerful GPU server.  Using a typical $1,200 GPU server we can build a model file in around five minutes.  This file is then transferred back to the DonkeyCar for autonomous driving.

#### Tubs
This is the term that the DonkeyCar software uses to store training data.  Each tub consists of a catalog of information about the drive and the images associated with that drive.

Note that the format of the tubs changes over time so old tubs formats may need to be converted to newer formats.

* [Script to Convert Tugs from V1 format to V2 Format](https://github.com/autorope/donkeycar/blob/dev/scripts/convert_to_tub_v2.py)
* [DonkeyCar Catalog Format](#tub-catalog)

#### Tub Catalog Format

Each Tub is a directory (folder) has two components:

1. A sub folder called "images" that contains the jpeg images gathered during a training run.  There are typically 10,000 to 20,000 small images in a tub image folder.
2. A file that describes the data about all the images called a Catalog file.  The Catalog file is similar to a JSON file but it has no root data elements.

#### NVIDIA Nano

One of the two single board computers we use in our DonkeyCars.  The current Nanos have 4GB RAM and a GPU for accelerating real-time inference.

The full product name is the NVIDIA Jetson Nano.

The price for a 4GB Nano is around $99 but they occasionally go on sale for $79.  The Nano became available for sale in the US in April of 2019.  A 2GB version has also been sold for $59 but the lack of RAM memory makes it difficult to use for many of our AI Racing League events and we don't recommend it.

Note that we do not use the Nano for training.  We transfer the data to a GPU server that has more parallel cores for training.

