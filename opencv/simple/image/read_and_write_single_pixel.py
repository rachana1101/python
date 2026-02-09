import cv2 as cv 
import os 
import matplotlib.pyplot as plt 

# OpenCV reads images in BGR format (Blue-Green-Red) instead of RGB due to historical reasons from its early development days.

# Why BGR?

# 1990s camera hardware: Most camera manufacturers and video capture cards stored pixels as BGR

# Windows COLORREF: Microsoft used 0x00bbggrr format (BGR order) in early Windows APIs

# BMP format: Windows bitmap files used BGR on disk


def readAndWriteSinglePixel(): 
    """
    Loads an image using OpenCV (BGR format), converts to RGB for matplotlib display.
    
    Demonstrates:
    - Path construction with os.path.join() for cross-platform compatibility
    - OpenCV BGR → RGB color conversion (critical for matplotlib)
    - Basic matplotlib image display
    """
    
    # Get current working directory - makes paths relative and portable
    root = os.getcwd()
    
    # Construct full image path - os.path.join handles / vs \ automatically
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # cv.imread() loads in BGR color order (NOT RGB) - OpenCV default
    image = cv.imread(imagePath)
    
    # CRITICAL: Convert BGR→RGB since matplotlib expects RGB
    # Without this, colors appear wrong (blue↔red swapped)
    imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Create new figure window
    plt.figure()
    
    # Display RGB image - now colors are correct
    plt.imshow(imageRGB)
    plt.title('Cute Cat (RGB)')
    plt.show()


if __name__ == '__main__':
    """
    Standard Python idiom - only runs function when script executed directly
    (not when imported as module)
    """
    readAndWriteSinglePixel()
