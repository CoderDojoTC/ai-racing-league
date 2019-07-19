# Community
Here are some sites that are of interest:

* [DonkeyCar web site](http://donkeycar.com)
* [AI Racing League Meetup Site](https://www.meetup.com/Artificial-Intelligent-Racing-League/)
* [CoderDojo St. Paul](https://wiki.coderdojosaintpaul.org/wiki/Main_Page)
* [Twin Cities AI Racing League](https://www.meetup.com/Artificial-Intelligent-Racing-League/)

# Hardware
**Hardware Options:** Raspberry Pi 3, 4, the Nvidia Nano, the Nvdia DX2, and the Intel Mobius Neural Stick
The base DonkeyCar today uses the Raspberry Pi 3+ which has a list price of $35.  This hardware is just barly able to process images in real-time in ide

The Nvidia Nano on the other hand has 128 CUDA core processors and has more than enough power to drive around a track in real time with varied lighting

The Intel Mobius stick is a low-power way to do image recognition using a USB dongle to do the image processing.  It would cost $75 in additon to the Ra

There are also college-level autonomous driving teams that use the more expensive Nvidia DX2 hardware.

**Nvidia Nano**<br />
Jetson Nano References
* [Donkey Car Nano Setup Page](https://docs.donkeycar.com/guide/robot_sbc/setup_jetson_nano/)
* [Joseph Bastulli PyTorch Nano](https://github.com/bastulli/AutoCarJetsonNano)
* [Nvidia Jetson Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
* [Nvidia Jetson Nano Kaya Video](https://www.youtube.com/watch?v=X3qGDYie1_I)

**Nvidia Nano Parts List**


| Part Name                         | Description                                                                                                                                                                                | Price      | Link                                                                                                                   | Note                                                                         |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| 128GB microSD card                | Samsung 128GB 100MB/s (U3) MicroSDXC Evo Select Memory Card with Adapter (MB-ME128GA/AM)                                                                                                   | $20        | https://www.amazon.com/Samsung-MicroSD-Adapter-MB-ME128GA-AM/dp/B06XWZWYVP                                             | MicroCenter in St. Louis Park has these for about 1/2 the prices             |
| Camera                            | Raspberry Pi Camera Module V2-8 Megapixel,1080p                                                                                                                                            | $30        | https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS                                              | MUST be Module V2. The V1 will NOT work with the Nano.                       |
| Dupont Connectors (F-F)           | EDGELEC 120pcs 20cm Dupont Wire Female to Female Breadboard Jumper Wires 3.9 inch 1pin-1pin 2.54mm Connector Multicolored Ribbon Cables DIY Arduino Wires 10 15 20 30 40 50 100cm Optional | $8 for 120 | https://www.amazon.com/EDGELEC-Breadboard-1pin-1pin-Connector-Multicolored/dp/B07GCY6CH7                               | Only need one of these                                                       |
| Nvidia Nano Single Board Computer | NVIDIA Jetson Nano Developer Kit                                                                                                                                                           | $99        | https://www.amazon.com/NVIDIA-Jetson-Nano-Developer-Kit/dp/B07PZHBDKT                                                  | Ships in two days                                                            |
| Power for Pi - 6700mAh            | Anker [Upgraded to 6700mAh] Astro E1 Candy-Bar Sized Ultra Compact Portable Charger, External Battery Power Bank, with High-Speed Charging PowerIQ Technology                              | $24        | https://www.amazon.com/Anker-Upgraded-Candy-Bar-High-Speed-Technology/dp/B06XS9RMWS                                    | I like this one but there are other variations. Some are rated at 10,000 mAh |
| Power Supply for Nano             | SMAKN DC 5V/4A 20W Switching Power Supply Adapter 100-240 Ac(US)                                                                                                                           | $10        | https://www.amazon.com/SMAKN-Switching-Supply-Adapter-100-240/dp/B01N4HYWAM                                            | Note that this is a 4A 12V power supply.                                     |
| RC Car                            | 1/16 2.4Ghz Exceed RC Magnet Electric Powered RTR Off Road Truck Stripe Blue NEW                                                                                                           | $119       | https://www.ebay.com/itm/1-16-2-4Ghz-Exceed-RC-Magnet-Electric-Powered-RTR-Off-Road-Truck-Stripe-Blue-NEW/223337258165 | E-Bay                                                                        |
| Wifi USB Dongle |
N150 USB wireless WiFi network Adapter for PC with SoftAP Mode - Nano Size, Compatible with Linux Kernal 2.6.18~4.4.3 (TL-WN725N) |                                          https://www.amazon.com/TP-Link-TL-WN725N-wireless-network-Adapter/dp/B008IFXQFU/                                                                                                          | $7         | I purchased one at Microcenter and it worked out-of-the-box on the Nano.  The Ubuntu drivers are pre-loaded!                                                                                                                       |                                                                              |
| Servo Module                      | HiLetgo 2pcs PCA9685 16 Channel 12-Bit PWM Servo Motor Driver IIC Module for Arduino Robot                                                                                                 | $10 for 2  | https://www.amazon.com/gp/product/B07BRS249H/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1                          | Note the quantity is 2                                                       |
