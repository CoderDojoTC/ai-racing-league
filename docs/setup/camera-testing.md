# Testing the Camera

To test the camera and cable, we need a command that captures video from a CSI camera connected to an NVIDIA Jetson Nano, converts the video format and resolution, and then displays the video on the screen.  We will
use the GStreamer command first.

## GStreamer Test on the Nano

```sh
$ gst-launch-1.0 nvarguscamerasrc sensor_mode=0 ! 'video/x-raw(memory:NVMM),width=3820, height=2464, framerate=21/1, format=NV12' ! nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=616' ! nvvidconv ! nvegltransform ! nveglglessink -e
```

This command is a GStreamer command used to test the functionality of a camera on a NVIDIA Jetson Nano device. GStreamer is a multimedia framework that provides a pipeline for media data. The `gst-launch-1.0` utility is used to build and run basic GStreamer pipelines.

Here's a breakdown of the command:

1. `nvarguscamerasrc sensor_mode=0`: This is a GStreamer plugin specific to the NVIDIA platform that provides support for the Camera Serial Interface (CSI) cameras. `sensor_mode=0` indicates that the command should use the first sensor mode of the camera. The sensor mode usually defines properties such as the resolution and frame rate that the camera supports.

2. `'video/x-raw(memory:NVMM),width=3820, height=2464, framerate=21/1, format=NV12'`: This part of the command specifies the desired output from the camera source. The properties indicate that the video should be in NV12 format, with a resolution of 3820x2464 pixels and a frame rate of 21 frames per second. NVMM refers to NVIDIA's proprietary multimedia memory.

3. `nvvidconv flip-method=0`: This is another NVIDIA specific GStreamer plugin that converts video from one format to another. The `flip-method=0` option means that no flipping operation should be performed on the frames. 

4. `'video/x-raw,width=960, height=616'`: This specifies the desired output format and resolution after the conversion. The resolution is downscaled to 960x616 pixels.

5. `nvvidconv ! nvegltransform ! nveglglessink -e`: This part of the pipeline takes the video from the conversion, applies an EGLStream transformation (`nvegltransform`) and then sends it to a EGL/GLES-based render sink (`nveglglessink`). This sink displays the video on the device's screen. The `-e` flag at the end of the command tells GStreamer to send an end-of-stream signal when the source stops, which will properly close down the pipeline.

### Why "!" and not "|"?

In the context of a GStreamer command, the "!" (aka bang) character is used to connect different elements of a GStreamer pipeline together. It serves a similar role to the UNIX "|" (pipe) character in a regular UNIX shell command, where it's used to pipe the output from one command into another.

However, there's an important difference between the two. In a UNIX shell command, the | character sends the standard output (stdout) of one command to the standard input (stdin) of another. In a GStreamer pipeline, the ! character doesn't simply pipe data from one element to the next. Instead, it establishes a connection between two GStreamer elements, allowing them to negotiate formats, buffer management, and other details. This negotiation process can involve more complex operations like format conversion, and it happens before any data is actually transferred.

So, in summary, while | and ! might seem similar, the latter is used in GStreamer to create more complex, negotiated connections between different multimedia processing elements.

### Flip Modes

The `flip-method` property of the `nvvidconv` (NVIDIA Video Converter) plugin controls the orientation of the output video in the NVIDIA Jetson platform. This is useful for handling scenarios where the camera could be mounted in various orientations.

Here are the possible values for the `flip-method` parameter:

- `0` (Identity) - No rotation, no vertical flip.
- `1` (Counterclockwise) - Rotate counter-clockwise 90 degrees.
- `2` (Rotate 180) - Rotate 180 degrees.
- `3` (Clockwise) - Rotate clockwise 90 degrees.
- `4` (Horizontal Flip) - Flip horizontally.
- `5` (Upper Right Diagonal) - Flip across upper right/lower left diagonal.
- `6` (Vertical Flip) - Flip vertically.
- `7` (Upper Left Diagonal) - Flip across upper left/lower right diagonal.

Each number corresponds to a specific operation on the video frames. The specific operation will be applied to each frame of the video before it's sent to the next element in the GStreamer pipeline.



## Resources

### Dan's Blog 

[NVIDIA CSI Camera GitHub Repo](https://github.com/JetsonHacksNano/CSI-Camera)

### Jetson Hacks Blog

https://jetsonhacks.com/2019/04/02/jetson-nano-raspberry-pi-camera/