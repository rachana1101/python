import cv2 as cv      # OpenCV for BGR image loading and channel operations
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for subplot grid display
import numpy as np    # NumPy for array matching with zeros_like()

def hsv_color_segmentaton(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux path separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Loads color image in BGR format (OpenCV default); returns None if file missing
    image = cv.imread(imagePath)
    imageInRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # Convert BGR→RGB for Matplotlib (unused here)

    # **KEY STEP**: Convert BGR image to HSV color space for better color-based segmentation
    # HSV = Hue (color), Saturation (intensity), Value (brightness)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    
    # Define HSV range for target color (likely pinkish cat skin/nose):
    # Hue: 0-10 (red-pink range, 0-180 scale)
    # Sat: 0-120 (low-medium saturation)  
    # Val: 0-150 (dark-medium brightness, avoids white fur)
    lower_bound = np.array([0, 0, 0])      # Min HSV values
    upper_bound = np.array([10, 120, 150]) # Max HSV values
    
    # **COLOR MASKING**: Creates binary mask (white=match, black=no match)
    # Pixels within HSV bounds → WHITE (255); outside → BLACK (0)
    mask = cv.inRange(hsv, lower_bound, upper_bound)

    # Display original BGR image using Matplotlib (shows BGR colors, appears reddish)
    plt.figure()
    plt.imshow(image)  # Note: BGR → looks wrong in matplotlib
    plt.show()

    # Display binary mask using OpenCV window (white=detected color, black=ignored)
    cv.imshow('mask', mask)
    cv.waitKey(0)  # Waits for keypress; closes on any key
    cv.destroyAllWindows()  # Clean up OpenCV windows (missing in original)

if __name__ == '__main__': 
    hsv_color_segmentaton()
