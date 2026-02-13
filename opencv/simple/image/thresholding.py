# | Gaussian Blur                          | Thresholding                     |
# | -------------------------------------- | -------------------------------- |
# | Smooths image (continuous values)      | Segments image (binary/discrete) |
# | Weighted average of neighbors          | Hard if/then decision per pixel  |
# | Output: 0-255 range (smooth gradients) | Output: 0 or 255 (black/white)   |
# | cv.GaussianBlur()                      | cv.threshold()                   |
#
# Original:     Gaussian (σ=8):      Threshold (70):
# [Full color]    [Soft dreamy cat]    [Black/white cat silhouette]
#   😺             😸                 ⬜😺⬛
#
# When to use each
#  Gaussian blur: Remove noise, smooth skin, prep for segmentation
#  Thresholding: Extract objects, create masks, binarize documents

import cv2 as cv      # OpenCV for image loading and histogram calculation
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for image display and plotting
import numpy as np    # NumPy for array operations (unused here but good practice)

def thresholding(): 
    # Get current working directory where script is located
    root = os.getcwd()
    
    # Build cross-platform path to cutecat.jpg (works on Windows/Linux/Mac)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Load image as GRAYSCALE (single channel, 0-255 intensity values)
    # cv.IMREAD_GRAYSCALE converts color → single intensity channel
    image = cv.imread(imagePath, cv.IMREAD_GRAYSCALE)
    
    # Calculate HISTOGRAM: how many pixels have each intensity (0-255)
    # [image] = image array, [0] = channel 0 (grayscale), None = no mask
    # [256] = 256 bins, [0,256] = range 0→256
    hist = cv.calcHist([image], [0], None, [256], [0,256])
    
    # Plot histogram: X-axis = intensity (0=black→255=white), Y-axis = pixel count
    plt.figure()
    plt.plot(hist)
    plt.xlabel('bin')      # Intensity value (0-255)
    plt.ylabel('# of pixels')  # How many pixels have that intensity
    plt.show()
    
    # plt.imshow(image, cmap='gray')  # Shows original grayscale image

    # Define 5 different thresholding TYPES OpenCV supports
    thresOpt = [cv.THRESH_BINARY,      # >70→255, ≤70→0
                cv.THRESH_BINARY_INV,  # >70→0, ≤70→255 (inverted)
                cv.THRESH_TOZERO,      # >70→original, ≤70→0
                cv.THRESH_TOZERO_INV,  # >70→0, ≤70→original (inverted)
                cv.THRESH_TRUNC]       # >70→70, ≤70→original (caps at 70)

    # Human-readable names for each thresholding method
    thresNames = ['binary', 'binaryInv', 'toZero', 'toZeroInv', 'trunc']

    # Create 2x3 subplot grid for visualization (6 total images)
    plt.figure()
    plt.subplot(231)  # Row2, Col3, position 1: ORIGINAL image
    plt.imshow(image, cmap='gray')
    plt.title('Original')

    # Loop through 5 thresholding types, apply each one
    for i in range(len(thresOpt)): 
        # subplot(2,3,i+2): positions 2,3,4,5,6 for 5 thresholded versions
        plt.subplot(2, 3, i+2)
        
        # Apply threshold: image, threshold=70, maxval=255, type=thresOpt[i]
        # Returns (retval, thresholded_image) - we ignore retval
        _, imgThres = cv.threshold(image, 70, 255, thresOpt[i])
        
        # Display thresholded result with method name as title
        plt.imshow(imgThres, cmap='gray')
        plt.title(thresNames[i])
        plt.axis('off')  # Hide axes for cleaner look

    plt.tight_layout()  # Auto-adjust subplot spacing
    plt.show()

# Run when script executed directly (not imported)
if __name__ == '__main__':
    thresholding()
