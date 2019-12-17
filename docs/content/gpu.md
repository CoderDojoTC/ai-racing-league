# GPU

# Design Goals
We wanted to create a system that had fast training times but was portable so that we can easily carry it in a car and ship
it to remote events.  Here are our design objectives.
## Fast Training Times
We want students to be able to drive around a track 20 times (10 times clockwise and 10 times counterclockwise) and
generate a reasonable sized data set of 20 frames per second and 224X224 images.  We want to train with this
data set in under five minutes.  This means that we want to use a GPU card that has about 2000 CUDA cores.
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
We wanted students to be able to look into the case and see the parts.

# Sample Parts List

# Fast Training Times for budget of $2,300
[Jon Herke's Tiny Monster](https://pcpartpicker.com/user/Herk89/saved/ypHZf7)

| Part Name                         | Description                                                                                                                                                                                | Price      | Link                                                                                                                   | Note                                                                         |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CPU |  	AMD Ryzen 5 3600 3.6 GHz 6-Core Processor | $189.99 | Link | Notes
| Motherboard | Gigabyte X570 I AORUS PRO WIFI Mini ITX AM4 | $219.99 | Link | Notes
| RAM |  Corsair Vengeance RGB Pro 32 GB (2 x 16 GB) DDR4-3200 Memory | $162.99 | Link | Notes
| Storage |  	Gigabyte AORUS NVMe Gen4 1 TB M.2-2280 NVME Solid State Drive | $209.99 | Link | Notes
| Cooling |  Cooler Master MasterLiquid ML120R RGB 66.7 CFM Liquid CPU Cooler | $103.86 | Link | Shoud we reconsider a liguid cooling system when the GPU could be left out in a car in freezing temperatures?
| GPU Card | NVIDIA GeForce RTX 2080 Ti 11 GB Founders Edition Video Card | $1199.99 | Link | 4000 CUDA cores makes for fast training
| Case | Lian Li TU150 Mini ITX Desktop Case | 	$109.99 | Link | We love the handle on this small case and the glass side panel.
| Power Supply | Corsair SF 600 W 80+ Gold Certified Fully Modular SFX Power Supply | $114.99 | Link | Is 600W really needed?
