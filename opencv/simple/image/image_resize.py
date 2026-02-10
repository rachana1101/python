import cv2 as cv      # OpenCV for BGR image loading and resizing
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for subplot grid display
import numpy as np    # NumPy for array operations

def image_resize(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux path separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Loads color image in BGR format → converts to RGB for Matplotlib display
    image = cv.imread(imagePath)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # **CROP** a small region from original image (y1:y2, x1:x2, all channels)
    # Extracts 145×89 pixel patch (likely cat's face) for clearer resizing comparison
    image = image[200:345, 300:389, :]  # shape becomes (145, 89, 3)

    height, width, _ = image.shape  # Unpack dimensions (ignores channels)

    scale = 4  # Upscale factor: new_size = original × 4

    # List of 5 OpenCV interpolation methods for comparison
    interpMethods = [
        cv.INTER_AREA,    # Pixel area resampling (best for downscaling)
        cv.INTER_LINEAR,  # Bilinear (OpenCV default, good balance)
        cv.INTER_NEAREST, # Nearest neighbor (fastest, blocky)
        cv.INTER_CUBIC,   # Bicubic (high quality upscaling)
        cv.INTER_LANCZOS4 # Lanczos (sharpest, slowest)
    ]

    interpTitle = ['area', 'linear', 'nearest', 'cubic', 'lanczos']  # Short names for titles

    plt.figure()  # New figure for 2×3 subplot grid
    
    # subplot(2,3,1): ORIGINAL image (position 1)
    plt.subplot(2, 3, 1)
    plt.imshow(image)
    plt.title('Original')  # Missing title in original code

    # Loop: Resize + display each method in positions 2-6
    for i in range(len(interpTitle)):
        plt.subplot(2, 3, i+2)  # Positions: 2,3,4,5,6
        
        # **RESIZE**: 4x larger using different interpolation method
        # New size: (width×4, height×4) = smooth upscaling test
        imgResize = cv.resize(image, (int(width*scale), int(height*scale)),
                              interpolation=interpMethods[i])
        plt.imshow(imgResize)
        plt.title(interpTitle[i])  # Label each method
    
    plt.tight_layout()  # Auto-adjust spacing (recommended)
    plt.show()    

if __name__ == '__main__':
    image_resize()
