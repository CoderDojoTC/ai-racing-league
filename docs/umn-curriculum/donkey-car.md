## Getting Familiar with Donkey Car

Donkey Car is an open source DIY autonomous RC car. It uses Python and TensorFlow to drive autonomously and is a great way to learn about machine learning, robotics, and systems integration.

### Donkey Car Parts

The main components of the Donkey Car setup include:

- **The Raspberry Pi:** Acts as the brain of the car, handling computations, camera input, and steering decisions.
- **The Camera:** Captures images that are used by the neural network to make driving decisions.
- **The Motor HAT:** An add-on for the Raspberry Pi that allows it to control and drive the motors.
- **The Chassis:** The physical body of the car including motors, wheels, and the frame.
- **The Battery:** Powers the Raspberry Pi and the motors.

### The Raspberry Pi

- The Raspberry Pi is a small, affordable computer that you can use to learn programming through fun, practical projects. For the Donkey Car, it is mounted on the car and connected to the other components to control them.

### The Pulse Width Modulation Board (PWM)

- The PWM board is used to control the speed and direction of the motors. It converts digital signals from the Raspberry Pi into analog signals that can drive the motors.

### The Motor and Servo

- **The Motor:** Powers the car's movement forward and backward.
- **The Servo:** Controls the steering by adjusting the wheels' angle.

### The Power System

- The Donkey Car typically uses a LiPo battery to power the motors and a USB power bank to power the Raspberry Pi.

---

## Hardware Setup

Setting up the Donkey Car involves assembling the chassis, mounting the Raspberry Pi, connecting the motor and servo to the PWM board, and ensuring all parts are powered correctly.

### Wiring Diagram

A basic wiring diagram includes:

- Connections from the Raspberry Pi GPIO pins to the PWM board.
- Connections from the PWM board to the motor and servo.
- Power supply connections to both the Raspberry Pi and the motors.
