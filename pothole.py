import cv2
import numpy as np

# Load the image (make sure the filename is correct and in the same directory)
image_path = 'D:\Project\Projects For Interview\Pothole\Pothole-Detector-using-Image-Processing\pot.jpg'  # or 'images/pot.jpg' if it's in a subfolder
image = cv2.imread(image_path)

# Check if image loaded successfully
if image is None:
    print(f"Error: Could not load image from {image_path}. Please check the file path.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Display the edge-detected image in a window
    cv2.imshow("Pothole Edge Detection", edges)
    cv2.waitKey(0)  # Waits for a key press to close the window
    cv2.destroyAllWindows()
