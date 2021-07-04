# AI Racing League GPU Components

# Design Goals
We wanted to create a local training system that had fast training times but was portable so that we can easily carry it in a car and ship
it to remote events.  We can't assume any connectivity to the Internet for our events since some of them might
be held in parking lots with no network access.  Here are our design objectives.

## Fast Training Times
We want students to be able to drive around a track 20 times (10 times clockwise and 10 times counterclockwise) and
generate a reasonable sized data set of 20 frames per second and 224X224 images.  This ends up being about 10,000 images.  The sizes are a bit larger for larger tracks and slower drivers.

We want to train with this data set in under five minutes.  This means that we want to use a GPU card that has about 2000 CUDA cores.
An example of this is the Nvidia GTX graphic cards.  [The RTX 2080](https://www.nvidia.com/en-us/geforce/graphics-cards/rtx-2080) which currently has a list price of around $1,200.  This puts the card at over half the price of our systems.

A lower cost option is the RTX 2070 which has a retail list price of around $500 USD.  The benchmarks for image training for these two boards were done by Dr Donald Kinghorn in March of 2019.  [His analysis]
(https://www.pugetsystems.com/labs/hpc/TensorFlow-Performance-with-1-4-GPUs----RTX-Titan-2080Ti-2080-2070-GTX-1660Ti-1070-1080Ti-and-Titan-V-1386/) shows that a single GTX 2080 Ti can process about 293 images per second.  The GTX 2070 only does about 191 images per second.  So for 

## Small and Lightweight
We originally were "gifted" a somewhat old GPU server used in a data center for training deep learning models.  Although
the sever was "free", it was over 70 pounds and had far more capability for RAM and power then we needed at events.
Based in this experience we opted to build a much smaller system using a mini enclosure with a handle.
We selected the Mini ITX Desktop Case and determined that we could still fit the GPU in this case.

## Rugged
Must be able to take the bumps of shipping and be able to be left out in a car overnight in freezing temperatures.
This was a requirement for remote events in rural Minnesota communities.  We opted for a full SSD drive to keep the moving
parts to a minimum.

## Easy to ship to remote sites
We had to be able to put the unit is a remote shipping case.

## Visibility
We wanted students to be able to look into the case and see the parts.  There is
a trend to also purchase RGB LED versions of components which we thought we could
program to change from RED to Green during the training process as the model
converges.  We have not found a good API for the parts so a simple $5 LED strip
on a Arduino Nano might be a better idea.  See the [Moving Rainbow](https://github.com/dmccreary/moving-rainbow) project for
sample designs.  We create these at the IoT hackthons each year.

# Sample Parts List

# Fast Training Times for budget of $2,300
[Jon Herke's Tiny Monster](https://pcpartpicker.com/user/Herk89/saved/ypHZf7)

| Part Name                         | Description                                                                                                                                                                                | Price      | Link                                                                                                                   | Note                                                                         |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CPU |  	AMD Ryzen 5 3600 3.6 GHz 6-Core Processor | $189.99 | Link | Notes
| Motherboard | Gigabyte X570 I AORUS PRO WIFI Mini ITX AM4 | $219.99 | Link | Notes
| RAM |  Corsair Vengeance RGB Pro 32 GB (2 x 16 GB) DDR4-3200 Memory | $162.99 | Link | Notes
| Storage |  	Gigabyte AORUS NVMe Gen4 1 TB M.2-2280 NVME Solid State Drive | $209.99 | Link | Notes
| Cooling |  be quiet! Dark Rock Pro 4, BK022, 250W TDP | $89.90 | https://www.amazon.com/dp/B07BY6F8D9/ref=cm_sw_r_cp_api_i_PYp-DbFCY51CH | We have also used a liquid cooler but we were worried about it freezing in cold
| High End GPU Card | NVIDIA GeForce RTX 2080 Ti 11 GB Founders Edition Video Card | $1199.99 | https://www.nvidia.com/en-us/geforce/graphics-cards/rtx-2080-ti/ | 4000 CUDA cores makes for fast training
| Cost Effrective GPU Card | NVIDIA GeForce RTX 2070 Ti 8 GB Founders Edition Video Card | $499.99 | https://www.nvidia.com/en-us/geforce/graphics-cards/rtx-2070-super/ | $500 price is a lower cost alternative
| Case | Lian Li TU150 Mini ITX Desktop Case | 	$109.99 | Link | We love the handle on this small case and the glass side panel.
| Power Supply | Corsair SF 600 W 80+ Gold Certified Fully Modular SFX Power Supply | $114.99 | Link | Is 600W really needed?

# Assembly
There are several good videos on YouTube that show how to assemble custom systems.  You can also use a search
engine to find videos for each of the parts.  The Liquid coolers can be tricky to install correctly if you
don't have experience.  We also recommend reading the user manauals for each of the parts.  They are usually on line.

# Drivers
We used the UNIX command line to install the drivers

A guide to do this is here:
[Installation of Nvidia Drivers on Ubuntu 18](https://www.linuxbabe.com/ubuntu/install-nvidia-driver-ubuntu-18-04)


