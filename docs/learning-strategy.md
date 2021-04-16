# AI Racing League Educational Philosophy

The AI Racing League educational philosophy is founded on the following values:

1. **Equal Opportunity** - we work hard to keep all AI Racing League activities free and we work hard to encourage girls to be part of our programs.
2. **Student driven** - we ask each student what their learning goals are and adapt to their needs
3. **Project based** - we prefer to let students define their own projects and we find resources to support them.  If learning about how to get a car to drive by itself that is great, but if they have other objectives we work hard to connect them with the mentor that will help them build whatever they are interested in building.
4. **Teamwork** - we want students to work in teams so they learn not just about AI, but how to work with others.
5. **Flexibility** - we want to be known as one of the most flexible learning organizations around.  We don't force everyone to learn the same things.  We take students in for 20 minutes or two years.  We adapt to the needs of our students and we design our curriculum around their needs.
6. **Agility** - in software there is a strong concept of "Agile Development" where team constantly get feedback on what works and adapt their goals every two weeks to meet the needs of their users.  We use these same strategies to develop flexible content to meet the ever-changing interests of our students.

Our Curriculum is based around building a series of concept cards that adhere to the "one concept per card" rule.  Each card is a 5.5in X 8in laminated card with questions or challenges on the front and answers on the back.  Concept cards have three difficulty levels with different colored borders.

1. **Green Borders** - Beginner cards that anyone can start with at any time
2. **Blue Borders** - Intermediate - where you may need to know some beginning concepts before you start
3. **Black Borders** - Advanced - where you need to master several intermediate concepts before you take these on

Our goal is to keep the concepts as "flat" as possible without a deep level of dependency.  We try to keep at least half of our cards mostly green beginner cards.

Students will walk into the AI Racing League and see a stack of cards.  They will pick up one card or a set of cards and work on these.  When they are done they return the cards and select another set of cards.

Because of our 

[Concept Cards in Google Docs](https://docs.google.com/presentation/d/1VKzVaDYbqKQ5ykSnNVem5_K7A-I5YtGPhbS73h1SrPI/edit?usp=sharing)

# Engineering Challenges
To develop a world class curriculum, we need to partner with senior engineers and curriculum developers.  Here are some of the challenges we need to address.

## Challenge #1: Make it easy for short term learning
Engineers with experience in both hardware and software can build their own DonkeyCar from parts in a few weeks, our goal is to allow students from a wide variety of backgrounds to be able to participate in events in a flexible way.  A typical CoderDojo event typically only lasts two hours and students may not have the appropriate background in hardware, Python programming or UNIX.

## Challenge #2: On site traning hardware
Many people that are building DonkeyCars use a standard Mac or PC laptop.  These systems take up to two hours to train a typical model - too long for many events.  One solution would be to leverage clound-based GPUs to accelerate learning.  This option typically requires transferring around 1/2 GB of images up to the clound for training the models.  Models, which can typically be 10MB, then need to be transferred back from the clound to the local car.  Our challenge here is that many locations may not have high-bandwith uploading and downloading services that could handle this traffic.

One solution is to acquire some robust GPUs that students can use to quickly train complex models - typically in 15 to 20 minutes.  This hardware needs to be easy to use - for example we need to do folder-based drag and drops and press a single button to begin training.

