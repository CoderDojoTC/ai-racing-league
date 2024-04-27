## Moving the Model to a Car

Before we start, let's clarify what we're doing. We've created a program
(or "model") that can control a car to drive by itself, kind of like a
video game character that knows how to navigate obstacles without you
touching the controls. Now, we want to take this program from our main
computer (let's call it the "Host PC") and put it onto the smaller
computer inside the car (we'll use "Raspberry Pi" for this). The
Raspberry Pi is like the car's brain, and we're going to teach it how to
drive on autopilot.

### Step 1: Connect Both Computers to the Same Network

-   **Why?** - For the Host PC to talk to the Raspberry Pi, they need to
    be on the same Wi-Fi network, like how two phones need to be on the
    same network to share photos.

-   **How?** - Follow the instructions in the "Networking" section to
    connect both devices to the same Wi-Fi. This is similar to how you
    connect your phone or laptop to your home Wi-Fi.

### Step 2: Check the Connection

-   **How?** - Open the "Terminal" on the Host PC. The Terminal is a
    place where you can type commands for your computer to follow.

-   **What to Type**: - Enter `ping <hostname>.local` but replace
    `<hostname>`; with your Raspberry Pi's hostname. This is like asking, "Hey, are you there?" to the
    Raspberry Pi.

-   **Expected Outcome**: - If everything is set up right, your computer
    will reply back with messages that show it's connected to the
    Raspberry Pi.

### Step 3: Send the Model to the Raspberry Pi

-   **What We're Doing**: - We're going to send the driving program (the
    model) from the Host PC to the Raspberry Pi.

-   **How?** - We use a command that packages up the model and sends it
    over the Wi-Fi to the Raspberry Pi.

-   **The Command**: - `rsync -rv --progress --partial <file path to model on Host PC> <username>@<hostname>.local:<(path to models/ folder on Pi)>`

    -   Breakdown:

        -   rsync is the tool we're using to send the file.

        -   `-rv --progress --partial` are options that make rsync show us
            what's happening and not quit halfway if there's a problem.

        -   `<file path to model on Host PC>` is where your model
            file is on your computer. You have to replace this with the
            actual path.

        -   `<username>@<hostname>.local` is the address of
            your Raspberry Pi on the network. Replace `<username>`;
            with your Raspberry Pi's username and `<hostname>` with
            its hostname.

        -   `<(path to models/ folder on Pi)>` tells rsync where
            on the Raspberry Pi to put the model. You'll replace this
            part with the actual location.
    
    ```bash title="Transfer Model Files from Host PC to the Pi"
    rsync -rv --progress --partial <file path to model on Host PC> <username>@<hostname>.local:<(path to models/ folder on Pi)>
    ```
    

-   **Important Note**:

    -   The model you've made works best with the car you trained it on.
        If you try to use it on a different car, it might not drive as
        expected. This is because the model has learned how to drive
        based on the specific car it was trained with.

-   **Example Command**:

    -   Here's an example of what the command might look like:

        -   `rsync -rv --progress --partial /home/arl/mycar/models/jon_model_1.tflite arl@donkeypi.local:~/mycar/models/`

        -   In this example, we're sending a model named
            `jon_model_1.tflite` from the Host PC to the Raspberry Pi,
            which is named donkeypi.

By following these steps, you'll transfer your autopilot model from your
Host PC to the Raspberry Pi, getting your model car ready to drive
itself!

## Driving Autonomously

Now that the models are on the Raspberry Pi, we are able to use them to
autonomously drive the Donkey Car. To do this, we follow steps similar
to the collection of the training data. However, we need to supply the
path to the model and the type of model to the Python program. Hence we
follow these steps:

### Step 1: Connecting the Devices to the Same Wi-Fi Network

-   **Why is this important?** Just like how your smartphone needs to
    connect to the internet to send pictures to your friends, the
    computer (which we'll call the Host PC) needs to be on the same
    Wi-Fi network as the Raspberry Pi to communicate with it.

-   **How to do it**: Check the section titled "Networking" in your
    materials. It will guide you on how to connect both your Raspberry
    Pi and Host PC to the same Wi-Fi network, similar to how you connect
    any device to your home internet.

### Step 2: Verifying the Connection

-   **How to check**: Open a program called "Terminal" on your Host PC.
    It's a tool where you can type commands to talk to your computer.

-   **What to do**: Type the command `ping <hostname>.local`, but
    replace `<hostname>` with your Raspberry Pi's unique name. This
    command is like saying, "Hey Raspberry Pi, can you hear me?".

-   **What to expect**: If everything is correct, you'll see messages
    that confirm your Host PC is talking to the Raspberry Pi.

### Step 3: Starting the Car's Driving Program

-   **What to do**: On your Raspberry Pi, open its Terminal and enter
    this command:  
    `python manage.py drive --js --model <path to your model> --type <model type>`  
    You'll need to replace `<path to your model>` with the location
    of the AI model file you're using (usually found in the `models/`
    folder). Replace `<model type>` with the kind of AI model you
    have, such as "Linear" or "Categorical".

    ```bash title="Start Driving with your Model"
    python manage.py drive --js --model <path to your model> --type <model type>
    ```
    

-   **For example**:  
    `python manage.py drive --model ~/mycar/models/mypilot.tflite --type tflite_linear`

### Step 4: Using the Web Controller to Drive

-   **How to access**: On your Host PC, open a web browser and go to
    `http://<hostname>.local:8887` — make sure to substitute
    `<hostname>` with your Raspberry Pi's name.

-   **Choosing the driving mode**: You'll see options like "User" for
    manual control, "Auto Steer" for the AI to only steer, and "Full
    Auto" for the AI to drive completely on its own. Select one and
    click “Start” to begin. If you're using a joystick, you can also
    start by pressing the start button.

-   **Safety first**: Before starting, ensure the Donkey Car is on its
    track with no obstacles around to prevent any accidents.

By following these steps, you'll be able to watch your Donkey Car
navigate its surroundings all by itself, thanks to the AI model you've
installed on the Raspberry Pi. It's a great way to see AI and machine
learning in action!