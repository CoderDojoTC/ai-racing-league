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
