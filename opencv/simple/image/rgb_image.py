import cv2 as cv      # OpenCV for BGR image loading and channel operations
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for subplot grid display
import numpy as np    # NumPy for array matching with zeros_like()

def bgrChannelColor(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux path separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Loads color image in BGR format (OpenCV default); returns None if file missing
    image = cv.imread(imagePath)
    # Splits BGR image into 3 separate 2D grayscale arrays: Blue, Green, Red channels
    b, g, r = cv.split(image)  # Unpacks channels in BGR order

    # Creates zero arrays matching blue channel's exact shape/dtype for masking
    zeros = np.zeros_like(b)  #np.zeros_like() creates a zero array matching an existing array's shape and dtype.
    # Isolates each channel: other channels set to black (0)

#     cv.merge(               # Function call needs outer ()
#     (b, zeros, zeros)       # Tuple: [array1, array2, array3] 
#     )                       # ← Three BGR channels

    bImg = cv.merge((b, zeros, zeros))     # Blue channel only (B=b, G=0, R=0)
    gImg = cv.merge((zeros, g, zeros))     # Green channel only (B=0, G=g, R=0) 
    rImg = cv.merge((zeros, zeros, r))     # Red channel only   (B=0, G=0, R=r)

    plt.figure()  # Creates new figure window
        
    plt.subplot(231)  # 2x3 grid, position 1 (top-left): Blue channel
    plt.imshow(bImg)  # Displays BGR → Matplotlib auto-converts to RGB view
    plt.title('Blue Channel')  # Shows intensity map of blue values

    plt.subplot(232)  # Position 2 (top-middle): Green channel  
    plt.imshow(gImg)
    plt.title('Green Channel')

    plt.subplot(233)  # Position 3 (top-right): Red channel
    plt.imshow(rImg)
    plt.title('Red Channel')
    
    plt.show()  # Renders and displays the 3-channel comparison grid

if __name__ == '__main__':
    bgrChannelColor()    
