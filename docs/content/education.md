# Concept Cards
Our cirruculim is based around building a series of concept cards that adhere to the "one concept per card" rule.  Each card is a 5.5in X 11in laminated card with questions or challenges on the front and anwers on the back.  Concept cards have three difficulty levels with different colored borders.

1. Green - Beginner
2. Blue - Intermediate
3. Black - Advanced

Students will walk into the AI Racing League and see a stack of cards.  They will pick up one card or a set of cards and work on these.  When they are done they return the cards and select another set of cards.

[Concept Cards in Google Docks](https://docs.google.com/presentation/d/1VKzVaDYbqKQ5ykSnNVem5_K7A-I5YtGPhbS73h1SrPI/edit?usp=sharing)

# Engineering Challenges
To develop a world class ciriculum, we need to partner with senior engineers and ciriculum developers.  Here are some of the challenges we need to address.

## Challenge #1: Make it easy for short term learning
Engineers with experience in both hardware and software can build their own DonkeyCar from parts in a few weeks, our goal is to allow students from a wide variety of backgrounds to be able to participate in events in a flexible way.  A typical CoderDojo event typically only lasts two hours and students may not have the appropriate background in hardware, Python programming or UNIX.

## Challenge #2: On site traning hardware
Many people that are building DonkeyCars use a standard Mac or PC laptop.  These systems take up to two hours to train a typical model - too long for many events.  One solution would be to leverage clound-based GPUs to accelerate learning.  This option typically requires transferring around 1/2 GB of images up to the clound for training the models.  Models, which can typically be 10MB, then need to be transferred back from the clound to the local car.  Our challenge here is that many locations may not have high-bandwith uploading and downloading services that could handle this traffic.

One solution is to acquire some robust GPUs that students can use to quickly train complex models - typically in 15 to 20 minutes.  This hardware needs to be easy to use - for example we need to do folder-based drag and drops and press a single button to begin training.

