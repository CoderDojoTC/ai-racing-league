# Hackathon Ideas
Here are a set of ideas that can be used to plan a Hackathon around the DonkeyCar.
Of course, if people are not familiar with the DonkeyCar, just getting it
to work is a good project!  These are more for teams that are extending
the DonkeyCar software.

# Beginner Projects - done in under one day
1. Ceate a UNIX shell script for managing the tub and model files.  The script
should present a menu of options that includes seending one or more tubs
to a server for training and getting the model file back.  Bonus points 
for listing models and sizes.
1. Build an RGB strip interface to display car and GPU status.
The car status can move from red to green as the number of images
gathered reaches a 10K image target.  Use the Arduino Moving Rainbow site
as your guide.  Background with Arduino is helpful.
1. Build an RGB strip interface to display the GPU training status.
The RGB strip should change from red to green as the model
error approaches a reasonable value like 0.01. Background with Arduino is helpful.
You will also need to modify the TensorFlow interface to write error values to
a serial port using python.

# Medium Projects - could be done with prep over a weekend
1. Ceate a web interface for managing the tub and model files.
The web interface should present a menu of options that includes seending one or more tubs
to a server for training and getting the model file back.  Bonus points for listing models and sizes.
1. Create a Jypyter notebook for analysing data and managing the tub and model files.
The web interface should present a menu of options that includes seending one or more tubs
to a server for training and getting the model file back.  Bonus points for listing models and sizes.

# Advanced Projects
1. Create a mobile application to drive the car during training.  
This is the best practice for many low-cost robots like the MiP.
Use the tilt APIs to make the car easy to steer.
1. Create small and large versions of the DonkeyCar.  The small version should
work on a 12x16 track and the large version should work outdoors on grass.
Use a Raspberry Pi or Nvidia Nano.
1. Create a learning management system for running AI Racing League events.
Create a list of concepts and load a dependancy list of concepts into
a graph database like TigerGraph.  Create a quiz that attendees use
to enter their learning objectives and background.  The app should
then recomend what content they should use, what tables they should visit,
and what mentors they should connect with in the right order.
Bonus points of you build a cell phone front end.


## Car to GPU File Transfer Scripts
Make it easy to transfer DonkeyCar test data to our GPU server.  Start with a UNIX shell script that
compresses the tub file and puts the data on a jump drive.  Then work on using SSH to copy the files
to the GPU server.  Then add configuration of the Avahi application and the mDNS protocols to autodiscover
the ARL GPU servers and prompte the user.

## Mobile App to Drive The Car
Most robot systems like the MIP have a simple mobile application for driving your robot around.  There are two modes:
A tilt mode (where you steer by tilting the phone) and a pressure mode where you can control the speed and direction
by pressing on a virtual joystick.  The problem we have with the current DonkeyCar 3.X system is that the web-based
application is difficult to use.  The tilt mode does not work on web browsers.  We suggest you use a program like AppInventor
for Android or Google Flutter and Dash building mobile apps.

## Leaderboard Web Page
Create a web application that tracks what teams are in the lead.  The app should be a single-page application that allows
team scores to be updated on a web form.  The leaderboard can also be "smart" a look for the team config files on each
DonkeyCar on the local-area network.

## OLED Extension
Add a low-cost OLED screen to each car using the SPI bus.  Have the OLED screen show key parameters such as hostname, static IP address,
disk space free, training data size etc.  Bonus points for a mode button to cycle through screens.  See Dan McCreary
for the hardware.

## LED Strips for Training Server Status
Add an low-cost WS-2811-B LED strip to the GPU server.  Make the strip blue when idle, red when you start training
an new model, and have it fade to green as the model converges.  See Dan McCreary for the hardware.

## Training Graph
As students walk in, give them a tablet to register.  It will also ask them basic questions.
It will then ask them how long they will be there.  It will then suggest a set of activities
and some concepts to master.  The graph is a dependacy graph of all the concepts we teach
at the event.  Also suggest a probability they will have fun at the event.

## Single Source Publishing for Concept Cards
Our cards need to be authored in MarkDown but we want to disply on the web, in PPT and with PDF.  To do this we want to adopt a single-source publishing pipeline.
