# Nano SD Image Checklist
This is a checklist that is genralized for all our events.  We can't assume any network connectivity at these events.

1. Image is based on the Nvidia Jetson
1. Swap file setup (at least 6 gig)
1. There is a user "donkey" with a password "car"
1. The default WiFi is setup and working for the event (use a guest account if we are at company site?)
1. The DonkeyCar 3.0 software installed consistently and tested
1. A virtual envinroment is setup and the user is set to that automatically at the end of the .basrc script
1. The CSI Camera demo is installed from the Jetson Hacks site to test the camera and do face recognition demos
1. The evtest program in installed to test the Logitech F710 joystick
1. The default config.py and myconfig.py are setup and customized for the CSI camera
1. The default image in the config.py file is 224X224
1. Chrome is the default browser
1. The "desktop" apps (word processing, spreadsheets, presentations) have been removed from the default dock
1. The Chrome browser and the Terminal are on the dock
1. The Chome bookmark bar is enabled (go to the Chrome Settings)
1. The latest version of OpenCV (cv2) is installed, compiled and tested
1. Jetson hacks
1. Decent python editor
1. Jupyter notebook support (arm version)
1. Sample Jupyter notebooks installed for viewing tub data and cleaning up the tub files (removing data with no speed)


# Unknowns
1. Can we write a menu-driven UNIX script that will automatically copy tubs to a GPU server and get a model back?
1. Can we assign static IP addresses and names to each car (dk1, dk2, dk3)
1. Can we assume that ALL cars use the same default calibration?
1. Can we write a short test script to verify that all the components are installed and working?
1. What standards should we have for the GPU servers (Ubuntu, not RedHat)
1. What other 
