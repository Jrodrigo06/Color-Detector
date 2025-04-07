import cv2

from PIL import Image
from utils import get_limits

light_blue = (70, 80, 50)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break


    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(light_blue)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)


    # Converting Image to PIL format
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    # Draw a rectangle around the detected object
    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)


    # Display the frame
    cv2.imshow('Frame', frame)
    

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

