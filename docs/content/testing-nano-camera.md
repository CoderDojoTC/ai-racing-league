# Testing the Camera on the Nvidia Nano

In this lab we will test the ability to stream a video image from the camera directly to the dispay using the CSI-Camera software on github.  We can test the camera on the Nvidia Nano by doing the following:

```
cd
mkdir projects
cd projects
git clond https://github.com/JetsonHacksNano/CSI-Camera
cd CSI-Camera
```
You can now create a UNIX shell script of the following:

Create the following file using either the nano editor or the vi command.

test-camera.sh
```
#!/bin/sh
gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM), width=3820, height=2464, framerate=21/1, format=NV12' \
! nvvidconv flip-method=2 ! 'video/x-raw,width=960, height=616' ! nvvidconv ! nvegltransform ! nveglglessink -e
```

Note that the flip-method has been changed from 0 to be 2 so that the image is rotated upright as it is mounted on the DonekyCar.

You can now make the test file executable

```
chmod 755 test-camera.sh
./test-camera.sh
```

You should now see the camera image on the screen.
