import cv2 as cv      # OpenCV for image loading and histogram calculation
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for image display and plotting
import numpy as np    # NumPy for array operations (unused here)

def gray_histogram(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux path separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # **LOAD GRAYSCALE DIRECTLY**: cv.IMREAD_GRAYSCALE loads as single-channel (no BGR conversion needed)
    image = cv.imread(imagePath, cv.IMREAD_GRAYSCALE)  # Shape: (H, W) not (H, W, 3)
    
    # Display grayscale image with proper colormap (matplotlib expects uint8 0-255)
    plt.figure()
    plt.imshow(image, cmap='gray')  # 'gray' colormap ensures correct black-white mapping

    # **CALCULATE HISTOGRAM**: cv.calcHist([images], [channels], mask, [bins], [range])
    # [image]     = source image (list format required)
    # [0]         = channel 0 (only channel for grayscale)  
    # None        = no mask (full image)
    # [256]       = 256 bins (one per intensity 0-255)
    # [0,256]     = pixel value range 0→255
    hist = cv.calcHist([image], [0], None, [256], [0,256])
    
    # New figure for histogram plot
    plt.figure()
    plt.plot(hist)  # hist.shape = (256,1) → x-axis auto 0-255, y-axis = pixel counts
    plt.xlabel('Pixel Intensity (0-255)')  # X: darkness → brightness
    plt.ylabel('# of Pixels')              # Y: how many pixels have that intensity
    
    plt.title('Grayscale Histogram')  # Missing in original
    plt.grid(True, alpha=0.3)         # Recommended: adds readability

    plt.show()  # Shows both figures

if __name__ == '__main__':
    gray_histogram()
