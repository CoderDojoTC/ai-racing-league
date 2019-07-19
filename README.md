<p align="center"> <img alt="logical" width="400px" src="/docs/assets/images/AIRL_logo.png" /> </p>

# Visit the Official Site 
https://coderdojotc.github.io/ai-racing-league/#/README

## About
This repository for a the AI Racing League - A fun way to learn AI using the Raspberry Pi and Python powered RC-cars.  Content includes mission, documentation, concept cards and sample labs.

Our documentation site is [here](https://coderdojotc.github.io/ai-racing-league)

## Summary
The AI Racing League is a project to create fun ways to learn the concepts around Artificial Intelligence (AI).  Our curriculum is inspired by the [DonkeyCar](https://www.donkeycar.com) which is a Raspberry Pi-based system built on a remote-control (RC) car chasis.

## Mission
Our mission is to create and deliver educational materials that will make fun AI training accessible to everyone. We place a special focus on students from disadvantaged communities including women and minorities.  We  work as a sub-project of the CodeSavvy not-for-profit organization and we adhere to their guildlines for quality and security of our students.  This means that all our volunteers have background checks and we limit the student to mentor ratios to no more than three students per mentor.  We are committed to equal opportunity mentoring.  We strive to recruit, train and retain the best mentors we can find.

## Concept Cards
Our cirruculim is based around building a series of concept cards that adhere to the "one concept per card" rule.  Each card is a 4.25in X 11in laminated card with questions or challenges on the front and anwers on the back.  Concept cards have three difficulty levels with different colored borders.

1. Green - Beginner
2. Blue - Intermediate
3. Black - Advanced

Students will walk into the AI Racing League and see a stack of cards.  They will pick up one card or a set of cards and work on these.  When they are done they return the cards and select another set of cards.

[Concept Cards in Google Docs](https://docs.google.com/presentation/d/1VKzVaDYbqKQ5ykSnNVem5_K7A-I5YtGPhbS73h1SrPI/edit?usp=sharing)

# Licensing
Like all CoderDojo created content, you are free to use this content in K-12 noncomercial educational settings for teaching without paying license fees.  We also encourge our community to create variations and help us enlarge the cirriculum.  We appreciate attribution.

Details of the license terms are here:
[Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0)

# Engineering Challenges
To develop a world class ciriculum, we need to partner with senior engineers and ciriculum developers.  Here are some of the challenges we need to address.

## Challenge #1: Make it easy for short term learning
Engineers with experience in both hardware and software can build their own DonkeyCar from parts in a few weeks, our goal is to allow students from a wide variety of backgrounds to be able to participate in events in a flexible way.  A typical CoderDojo event typically only lasts two hours and students may not have the appropriate background in hardware, Python programming or UNIX.

## Challenge #2: On site traning hardware
Many people that are building DonkeyCars use a standard Mac or PC laptop.  These systems take up to two hours to train a typical model - too long for many events.  One solution would be to leverage clound-based GPUs to accelerate learning.  This option typically requires transferring around 1/2 GB of images up to the clound for training the models.  Models, which can typically be 10MB, then need to be transferred back from the clound to the local car.  Our challenge here is that many locations may not have high-bandwith uploading and downloading services that could handle this traffic.

One solution is to acquire some robust GPUs that students can use to quickly train complex models - typically in 15 to 20 minutes.  This hardware needs to be easy to use - for example we need to do folder-based drag and drops and press a single button to begin training.

# Hardware Options: Raspberry Pi 3, 4, the Nvidia Nano, the Nvdia DX2, and the Intel Mobius Neural Stick
The base DonkeyCar today uses the Raspberry Pi 3+ which has a list price of $35.  This hardware is just barly able to process images in real-time in ideal lighting conditions and a well defined track.  There are now many other options that will allow us better performance.  The question is what option should we standardize on?

The Nvidia Nano on the other hand has 128 CUDA core processors and has more than enough power to drive around a track in real time with varied lighting conditions.  The list price is $99 and there seems to be widespread support for building cars using the Nano using both the traditional TensorFlow and the increasingly popular PyTorch.

The Intel Mobius stick is a low-power way to do image recognition using a USB dongle to do the image processing.  It would cost $75 in additon to the Raspberry Pi.  However, the software built around Intel's OpenVino libraries are complex to use and there is little on-line help.

There are also college-level autonomous driving teams that use the more expensive Nvidia DX2 hardware.

# References
Here are some sites that are of interest:

* [DonkeyCar web site](http://donkeycar.com)
* [AI Racing League Meetup Site](https://www.meetup.com/Artificial-Intelligent-Racing-League/)
* [CoderDojo St. Paul](https://wiki.coderdojosaintpaul.org/wiki/Main_Page)
* [Twin Cities AI Racing League](https://www.meetup.com/Artificial-Intelligent-Racing-League/)

Jetson Nano References
* [Donkey Car Nano Setup Page](https://docs.donkeycar.com/guide/robot_sbc/setup_jetson_nano/)
* [Joseph Bastulli PyTorch Nano](https://github.com/bastulli/AutoCarJetsonNano)
* [Nvidia Jetson Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
* [Nvidia Jetson Nano Kaya Video](https://www.youtube.com/watch?v=X3qGDYie1_I)

