Imagine your donkey car is a small, smart robot car that you can control
with a remote. To get it moving and learn how to switch between
different driving modes, you'll start with a simple command on your
computer. Here's how you do it:

1.  **Start the Car**: Open your computer's command line tool, type
    `python manage.py drive --js`, and press Enter. This wakes up your donkey
    car and gets it ready to follow your commands.

    ```bash title="Drive the Donkey Car"
    python manage.py drive --js
    ```
    

2.  **Understanding the Controls**: Right after you run the command,
    you'll see instructions pop up on your screen. These tell you which
    buttons on your controller do what. It's like learning the controls
    of a new video game. Make sure to jot these down or take a picture
    with your phone - you'll need to refer back to them!

3.  **Switching Driving Modes**: Your donkey car has a cool feature - it
    can drive in different ways! There's a special button (usually the
    start button) that lets you switch between:

    1.  **Fully Remote-Controlled Mode**: You control everything, just
        like driving an RC car.

    2.  **Fully Autonomous Mode**: The car drives all by itself, making
        its own decisions on turning and speed.

    3.  We'll focus on these two modes. If your controller doesn't seem
        to respond, hitting the start button is a good first
        troubleshooting step.

## Collecting Data for Your Car to Learn From

Now that your car can move around, it's time to teach it how to drive on
its own. This is done by collecting data - basically, you drive the car
around and it remembers how you did it. Here's how to gather good
learning material for your car:

1.  **Drive Around**: You'll need to drive your car around the track in both
    directions. Aim for about 10 laps each way. This gives your car a
    variety of examples to learn from.

2.  **It's Okay to Make Mistakes**: Try to keep the car within the track
    lines, but don't worry about staying perfectly centered all the
    time. In fact, it's good for your car to see how to recover from
    being off-center. This helps it learn to correct itself and makes it
    smarter at handling different situations.

Remember, the goal isn't to collect flawless data but to give your car a
rich learning experience, full of different scenarios and recoveries.
This way, your car becomes more adaptable and can handle the track like
a pro, even when things don't go exactly as planned.