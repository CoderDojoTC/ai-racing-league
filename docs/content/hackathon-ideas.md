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
