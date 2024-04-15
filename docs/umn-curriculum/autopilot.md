## Autopilot

Putting the trained model into action allows the Donkey Car to drive autonomously.

### Moving the Model to the Car

- **Transfer the Model:** Use SCP or a similar tool to transfer the trained model from your computer to the Raspberry Pi.
- **Configuration:** Ensure the model is correctly referenced in the car's configuration files.

### Driving Autonomously

- **Starting the Autopilot:** Use the command `python manage.py drive --model models/mypilot.h5` to start the car in autonomous mode.
- **Monitoring:** Initially, closely monitor the car's performance to ensure it operates safely and as expected.
