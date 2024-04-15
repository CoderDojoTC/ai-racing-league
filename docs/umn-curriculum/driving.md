## Driving Your Donkey Car and Collecting Data

Once your car is calibrated, the next step is to collect data that will be used to train the AI model for autonomous driving.

### Collecting Data for Your Car to Learn From

- **Driving the Car:** Use a controller to manually drive the car around a track. Try to cover various scenarios and track conditions.
- **Recording Data:** The Raspberry Pi automatically records images and driving inputs (throttle, steering) as data points.

### Data Quality Tips

- **Diverse Data:** Ensure the data includes different lighting conditions, various speeds, and multiple track layouts to create a robust dataset.
- **Avoiding Overfitting:** Include data where the car makes mistakes and corrects itself to help the model learn recovery strategies.
