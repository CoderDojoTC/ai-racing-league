# OpenCV Lab: Fun Face Filters**

**Objective:** Learn to detect faces using OpenCV and apply fun filters like cat whiskers and ears.

## Tools & Libraries
- Python
- OpenCV


## Haar Cascades

### Understanding Haar Cascades in OpenCV

**Haar Cascades** are a type of machine learning object detection method used to identify objects in images or video. In OpenCV, Haar Cascades are mainly used to detect faces, but they can also identify other objects like eyes, smiles, and more.  There were named after Hungarian mathematician [Alfréd Haar](https://en.wikipedia.org/wiki/Alfr%C3%A9d_Haar) who
make key contributions to the mathematics of transformation of matrix data in the 1920s.

Imagine you have a magic magnifying glass that you move across a photo. Whenever this magnifying glass sees a face, it lights up! That's kind of what Haar Cascades does in OpenCV.

### How Do Harr Cascades Work?

1. **Features**: Haar Cascades work by looking at simple features in an area of the image, like the bridge of the nose being brighter than the eyes on either side because it sticks out and catches the light.
2. **Training**: To make Haar Cascades 'learn' these features, it's shown many pictures of faces and non-faces. Through this, it learns what a face typically looks like.
3. **Cascade**: The term 'cascade' is used because the algorithm employs a series of increasingly complex features to determine if a particular region is a face.

### Building Face-Filters Using Haar Cascades:

Creating a Snapchat-like face filter using Haar Cascades involves two main steps:

1. **Face Detection**: Detecting the location of the face in an image or video stream.
2. **Overlaying the Filter**: Once we know where the face is, we can overlay our filter (like cat ears or sunglasses) at the correct position.

**Example Python Code**:

```python
import cv2

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the image
img = cv2.imread('your_photo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    # Here you'd typically overlay your filter, e.g., cat ears at coordinates (x, y)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Drawing a rectangle around the detected face for now

cv2.imshow('Face Detection', img)
cv2.waitKey()

**Resources:**
- Haarcascades for face and eye detection (provided by OpenCV).

**Steps:**

1. **Setup & Installation**
   
    Make sure you have Python and OpenCV installed.

    ```bash
    pip install opencv-python
    ```

2. **Face Detection**

   Before adding filters, students should understand face detection.

    ```python
    import cv2

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    img = cv2.imread('path_to_image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Detected Faces', img)
    cv2.waitKey()
    ```

3. **Designing the Filters**

   - Use any graphic software (like GIMP or Photoshop) to design transparent PNG images of cat whiskers and ears.
   - Ensure the filter graphics are adjustable in size or make several versions to fit different face sizes.

4. **Applying the Cat Ears Filter**

    Given the coordinates `(x, y, w, h)` of the detected face:

    ```python
    ear_image = cv2.imread('path_to_ear_image.png', -1)  # The -1 reads the alpha channel

    # Resize the cat ear image to fit the width of the face
    ear_width = w
    aspect_ratio = ear_image.shape[1] / float(ear_image.shape[0])
    ear_height = int(ear_width / aspect_ratio)
    ear_image = cv2.resize(ear_image, (ear_width, ear_height))

    # Region where we want to place the cat ears (taking care not to exceed image dimensions)
    for c in range(0, 3):
        img[y:y+ear_image.shape[0], x:x+ear_image.shape[1], c] = img[y:y+ear_image.shape[0], x:x+ear_image.shape[1], c] * (1 - ear_image[:, :, 3] / 255.0) + ear_image[:, :, c] * (ear_image[:, :, 3] / 255.0)
    ```

5. **Applying the Whiskers Filter**

    Similar to the cat ears, you can position whiskers on the cheeks using the `(x, y, w, h)` of the face.

6. **Real-time Filters Application**

    Capture video from the webcam and apply the filters in real-time.

    ```python
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            # Apply cat ears and whiskers filter here

        cv2.imshow('Filters in Action', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ```

7. **Challenge & Extension**

    - **Multiple faces:** Modify the code to handle multiple faces in one frame.
    - **Other Filters:** Allow students to design and implement their own filters.
    - **Interactivity:** Add buttons to change filters or toggle them on/off.

**Assessment:**

1. Can students successfully detect faces in different images?
2. How accurately do the filters get applied to the face?
3. How creative and effective are student-designed filters?

**Note:** This is a basic version and doesn't incorporate sophisticated technologies like deep learning which Snapchat uses. It's aimed at high school students to give a foundational understanding.
