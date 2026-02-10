import cv2 as cv      # OpenCV for image loading and histogram calculation
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for image display and plotting
import numpy as np    # NumPy for array operations (unused here)

def color_histogram(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux path separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    
    image = cv.imread(imagePath)  # Shape: (H, W) not (H, W, 3)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    image = image[200:345, 300:389, :] #capture specific area 

    
    # Display grayscale image with proper colormap (matplotlib expects uint8 0-255)
    plt.figure()
    plt.imshow(image)  # 'gray' colormap ensures correct black-white mapping

    colors = ['b', 'g', 'r']
    plt.figure()
    for i in range(len(colors)): 
        # **CALCULATE HISTOGRAM**: cv.calcHist([images], [channels], mask, [bins], [range])
        # [image]     = source image (list format required)
        # [i]         = channel
        # None        = no mask (full image)
        # [256]       = 256 bins (one per intensity 0-255)
        # [0,256]     = pixel value range 0→255
        hist = cv.calcHist([image], [i], None, [256], [0,256])
    
        # New figure for histogram plot
        
        plt.plot(hist)  # hist.shape = (256,1) → x-axis auto 0-255, y-axis = pixel counts
    plt.xlabel('Pixel Intensity (0-255)')  # X: darkness → brightness
    plt.ylabel('# of Pixels')              # Y: how many pixels have that intensity

    plt.title('RGB Histogram')  # Missing in original
    plt.grid(True, alpha=0.3)         # Recommended: adds readability

    plt.show()  # Shows both figures

if __name__ == '__main__':
    color_histogram()
