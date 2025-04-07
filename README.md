# Simple Color Detector with OpenCV

This project is a basic color detection tool that uses your webcam to detect a specified color range and draws a bounding box around any object matching that color in real-time.

## How It Works

- Captures webcam video feed using OpenCV.
- Converts each frame to HSV color space.
- Applies a color mask to detect objects of a specified color.
- Uses Pillow (PIL) to get the bounding box of the detected area.
- Draws a green rectangle around the detected object in the video feed.

### Code Explanation

- `cv2.VideoCapture(0)` opens the default webcam.
- The frame from the webcam is converted to HSV (Hue, Saturation, Value) color space using `cv2.cvtColor()`.
- `get_limits()` is a utility function that determines the lower and upper bounds for detecting the specified color in the HSV space.
- `cv2.inRange()` is used to create a mask for the specified color range.
- The mask is converted to a Pillow (PIL) image format to find the bounding box of the detected color.
- If the bounding box is found, a green rectangle is drawn around the detected object.