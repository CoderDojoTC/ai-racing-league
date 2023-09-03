# Bandwidth Calculation for 224x224 Color Images

## Objective

Calculate the total bandwidth needed for a camera that reads 224x224 color images and needs to write 10 images per second to the disk.

## Step-by-Step Calculation

### Step 1: Calculate the Size of a Single Image

A 224x224 color image would have \(224 \times 224 = 50,176\) pixels.

Assuming the image uses a standard RGB color scheme, each pixel would have three color channels: Red, Green, and Blue. Each channel typically requires 1 byte (or 8 bits) to store its intensity value.

So, each pixel would need 3 bytes.

The size of a single image would be:

\[
\text{Size of a single image} = \text{Number of pixels} \times \text{Bytes per pixel}
\]
\[
= 50,176 \, \text{pixels} \times 3 \, \text{bytes/pixel}
\]
\[
= 150,528 \, \text{bytes}
\]
\[
= 150.528 \, \text{KB}
\]
\[
\approx 0.147 \, \text{MB}
\]

### Step 2: Calculate the Total Bandwidth Needed Per Second

We are writing 10 images a second to the disk, so the total bandwidth needed per second would be:

\[
\text{Total bandwidth per second} = \text{Size of a single image} \times \text{Number of images per second}
\]
\[
= 150,528 \, \text{bytes/image} \times 10 \, \text{images/second}
\]
\[
= 1,505,280 \, \text{bytes/second}
\]
\[
= 1,505.28 \, \text{KB/s}
\]
\[
\approx 1.47 \, \text{MB/s}
\]

## Conclusion

The camera would need a total bandwidth of approximately \(1.47 \, \text{MB/s}\) to write 10 224x224 color images to the disk each second.
