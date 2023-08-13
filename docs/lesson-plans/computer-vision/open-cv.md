# OpenCV Labs

**Lesson Plan: Introduction to OpenCV in Python**

## Setup

Students should have access to a computer with a webcam and Python installed.  We use Rasberry Pi or NIVIDA Nanos with cameras.

**Objective:** By the end of the lesson, students will be able to explain the purpose and basic functions of OpenCV, and implement some basic image processing tasks.

---

## 1. Introduction (10 minutes)

- **Discussion**: Ask students if they've ever used Instagram or Snapchat filters, or how computers recognize faces or objects.
- **Explanation**: Introduce OpenCV as one of the most powerful libraries used for computer vision tasks. 

---

## 2. Brief History & Applications (10 minutes)

- Mention OpenCV's origins and its significance in AI and robotics.
- Showcase a few applications, e.g., facial recognition, self-driving cars, AR filters.

---

## 3. Basics of Image Representation (10 minutes)

- Discuss how computers see images as matrices of numbers.
- Quick overview: Images are made of pixels; each pixel has values that determine its color.

---

## 4. Installation & Setup (10 minutes)

- **Demo**: How to install OpenCV using `pip`.
  
      pip install opencv-python
  
- Quick navigation of the OpenCV documentation to encourage self-learning.

---

## 5. Hands-on Lab 1: Reading, Displaying, and Saving Images (20 minutes)

- **Exercise**: 
  1. Use OpenCV to read an image.
  2. Display the image in a window.
  3. Convert the image to grayscale.
  4. Save the grayscale image.

---

## 6. Hands-on Lab 2: Playing with Webcam Feed (20 minutes)

- **Exercise**:
  1. Access the webcam using OpenCV.
  2. Display the live video feed.
  3. Apply a grayscale filter to the feed.
  4. Bonus: Add a button or a keypress event to capture and save a snapshot from the feed.

---

## 7. Introduction to Basic Image Processing Techniques (15 minutes)

- **Explanation**:
  - Discuss image thresholding, blurring, and edge detection.
  - Showcase examples of each technique.

---

## 8. Hands-on Lab 3: Basic Image Processing (30 minutes)

- **Exercise**:
  1. Use a sample image (or one they choose).
  2. Apply and display thresholding.
  3. Apply and display blurring.
  4. Apply and display edge detection using the Canny edge detector.

---

## 9. Fun Lab: Snapchat-like Filters (45 minutes)

- **Objective**: The goal of this lab is to have students use OpenCV to create basic filters for a live webcam feed. 

- **Exercise**:
  1. Access the webcam feed.
  2. Overlay cartoon glasses or hats on the user's face using OpenCV's face detection (Haar cascades).
  3. Bonus: Let the students get creative, e.g., adding mustaches, changing background, etc.

---

## 10. Discussion & Wrap-up (15 minutes)

- Reflect on the potential of computer vision and its real-world applications.
- Discuss the ethical implications, such as privacy concerns with facial recognition.
- Introduce more advanced topics in OpenCV for those interested (like object recognition, machine learning with OpenCV, etc.)
- Q&A session.

---

## Additional Resources & Take-home Assignments:

1. **Explore More**: Give students links to OpenCV tutorials and documentation for further reading.
2. **Project**: Ask students to work on a mini-project, like a basic digital photo editor using OpenCV, allowing them to apply filters, rotate, and crop images.
3. **Challenge**: For advanced students, introduce them to object detection using pre-trained models in OpenCV.

---

## Notes for the Instructor:

- Make sure all students have Python installed and guide them in setting up a virtual environment.
- Visual aids, like slides with images representing pixel values, will help in explaining image representation.
- Encourage students to collaborate and share their findings or issues during labs. Pair programming can be useful.
- Make sure to have a few sample images ready for labs, preferably with varying complexities.
