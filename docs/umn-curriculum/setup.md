## Setting Up and Calibrating Your Donkey Car

Calibration is crucial for ensuring that your Donkey Car can drive as intended. Proper calibration involves adjusting the throttle and steering to respond correctly to commands.

### Step 1: Connecting to Your Car

- **Secure Connection Establishment:** Use SSH to securely connect your computer to the Raspberry Pi. This provides a command line interface for executing commands on the Pi.
- **Creating the Project Directory:** Use the command `donkey createcar --path ~/mycar` to set up the project structure.

### Step 2: Preparing for Calibration

- **Lift the Car:** Place the car on a stand so the wheels can rotate freely without moving the car.
- **Access Calibration Tools:** Utilize the Donkey Car utility `donkey calibrate` to start calibrating your car's throttle and steering.

### Step 3: Calibrating Throttle and Steering

- **Calibrating Throttle:** Adjust the throttle settings to find the neutral point where the car doesn't move, and then determine the forward and reverse speeds.
- **Calibrating Steering:** Adjust the steering settings to ensure the car can turn left and right correctly without oversteering.

### Step 4: Final Adjustments

- **Test Drive:** Place the car on the ground and test the throttle and steering adjustments. Make any final tweaks to ensure smooth operation.
