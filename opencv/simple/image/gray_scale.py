import cv2 as cv      # OpenCV for BGR image loading and channel operations
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for subplot grid display
import numpy as np    # NumPy for array matching with zeros_like()

def gray_scale(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux path separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Loads color image in BGR format (OpenCV default); returns None if file missing
    image = cv.imread(imagePath)
    imgGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    cv.imshow('gray', imgGray)
    cv.waitKey(0)
  
if __name__ == '__main__':
    gray_scale()    
