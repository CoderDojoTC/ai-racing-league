## Training

Training is the process where the collected data is used to teach the AI model how to drive the car autonomously.

### Step 1: Setting Up Your Computer for Training

- **Software Requirements:** Ensure Python and TensorFlow (or another ML framework) are installed on your computer.
- **Prepare the Data:** Transfer the collected data from the Raspberry Pi to your computer.

### Step 2: Training the Model

- **Initiating Training:** Use the Donkey Car command `donkey train --tub <data directory> --model ./models/mypilot.h5` to start the training process.
- **Monitoring Progress:** Training can take several hours. Monitor the progress for any errors or issues.

### Step 3: Evaluating the Model

- **Test the Model:** After training, test the model's performance by running it on the Donkey Car in a controlled environment.
- **Adjustments:** It may be necessary to retrain the model with additional data or make adjustments based on performance.
