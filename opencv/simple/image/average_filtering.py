import cv2 as cv      # OpenCV for image loading and histogram calculation
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for image display and plotting
import numpy as np    # NumPy for array operations (unused here)

def callback(): 
    pass

def average_filtering(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux path separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    
    image = cv.imread(imagePath)  # Shape: (H, W) not (H, W, 3)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)


    winName = 'avg filter'
    cv.namedWindow(winName)
    cv.createTrackbar('n', winName, 1, 100, callback)

    height, width, _ = image.shape
    scale = 1
    width = int (width * scale)
    height = int(height * scale)
    image = cv.resize(image, (width, height))

    while True: 
        if cv.waitKey(1) == ord('q'):
            break

        n = cv.getTrackbarPos('n', winName)
        imageFilter = cv.blur(image, (n,n))
        cv.imshow(winName, imageFilter)

    cv.destroyAllWindows()        


if __name__ == '__main__':
    average_filtering()    
