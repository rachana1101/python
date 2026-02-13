# | Gradient (cv.Sobel, cv.Laplacian)      | Thresholding (cv.threshold)    |
# | -------------------------------------- | ------------------------------ |
# | Input: Grayscale image                 | Input: Grayscale image         |
# | Output: Edge strength map (continuous) | Output: Binary regions (0/255) |
# | Math: Derivatives (intensity CHANGE)   | Math: If pixel > T then 255    |
# | Result: Bright lines = edges           | Result: Black/white blobs      |
# | Purpose: FIND boundaries               | Purpose: SEPARATE regions      |

import cv2 as cv      # OpenCV for image loading and gradient calculations
import os             # OS module for building platform-safe file paths
import matplotlib.pyplot as plt  # Matplotlib for 2x2 subplot display
import numpy as np    # NumPy for array operations (matrix multiplication)

def image_gradient(): 
    # Get current working directory where script runs
    root = os.getcwd()
    
    # Build cross-platform path to cutecat.jpg
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Load as GRAYSCALE (intensity only) - gradients work on single channel
    image = cv.imread(imagePath, cv.IMREAD_GRAYSCALE)

    # Create 2x2 subplot grid for visualization
    plt.figure()
    plt.subplot(221)  # Row2, Col2, position 1: ORIGINAL image
    plt.imshow(image, cmap='gray')
    plt.title('Original')

    # LAPLACIAN: 2nd derivative → finds regions of RAPID intensity change (edges)
    # cv.CV_64F = 64-bit float output (handles negative values)
    # ksize=21 = large kernel (21x21) for smoother gradients
    laplacian = cv.Laplacian(image, cv.CV_64F, ksize=21)
    plt.subplot(222)  # Position 2: Laplacian result
    plt.imshow(laplacian, cmap='gray')  # Bright = strong edges
    plt.title('Laplacian (2nd deriv)')

    # Get Sobel derivative kernels: dx=1 (x-direction), dy=0 (y-direction), ksize=3
    # kx = horizontal kernel, ky = vertical kernel (both 3x1 initially)
    kx, ky = cv.getDerivKernels(1, 0, 3)
    
    # Print kernel multiplication: shows how OpenCV combines kernels internally
    print(ky @ kx.T)  # Matrix multiplication → 3x3 Sobel X kernel

    # SOBEL X: 1st derivative in X direction (vertical edges)
    # dx=1 (horizontal deriv), dy=0 (no vertical), ksize=21 (large smoothing)
    sobelX = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=21)
    plt.subplot(223)  # Position 3: Sobel X result
    plt.imshow(sobelX, cmap='gray')
    plt.title('Sobel X (vertical edges)')

    plt.tight_layout()  # Auto-adjust subplot spacing
    plt.show()

if __name__ == '__main__':
    image_gradient()
