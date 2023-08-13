# AI Racing League Computer Vision Table

Raspberry Pi and the NVIDIA Nano are popular systems for demonstrating various computer vision applications due to their affordability and flexibility.

## Requirements

For these lessons, you just need a Raspberry Pi (or Nano) and the attached Camera that
we use for all our cars.

## Sample Labs

Here are several demos we show to high school students using OpenCV and Raspberry Pi:

### Face Detection and Recognition

We can use the built-in Haar cascades in OpenCV for face and eyes detection. For the face recognition part, you can use either OpenCV's built-in algorithms or deep learning-based models such as FaceNet.

### Object Detection

Use pre-trained models from OpenCV's DNN module or TensorFlow's model zoo to recognize multiple objects in real-time.

### Optical Character Recognition (OCR):

Combine OpenCV for image processing and Tesseract for character recognition to demonstrate how a device can read text from images or real-time video feed.

### Color Detection

Write a simple program that detects specific colors in real-time. This can be used as a stepping stone to more advanced object-tracking projects.

We can also combine this lab with our Raspberry Pi Pico color detection sensors.

### Motion Detection and Tracking

Implement a simple surveillance system that detects motion and tracks moving objects. This can be a good introduction to video analysis.

### Augmented Reality
Show how to overlay graphics on a real-time video feed based on detected features. For example, you can use OpenCV's capabilities for feature detection (like SIFT, SURF, ORB) and perspective transformation to overlay 3D objects on a marker.

### Hand Gesture Recognition
Create a program that recognizes hand gestures and associates them with commands. You could use this to control a game or navigate a user interface.

### License Plate Recognition
You can implement a simple Automatic Number Plate Recognition (ANPR) system using image processing techniques in OpenCV and OCR.

### QR Code and Barcode Scanner
Use OpenCV for real-time detection and decoding of QR codes and bar codes.

Most of these demonstrations will require additional Python libraries beyond just OpenCV, like NumPy, Pillow, or TensorFlow.

For hardware, you will need the Raspberry Pi 3 with 4GB RAM, a camera module, and potentially additional items like a monitor, mouse, and keyboard for a fully interactive setup.




