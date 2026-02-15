import cv2 as cv      # OpenCV for BGR image loading and filtering operations
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for subplot display
import numpy as np    # NumPy for random noise generation

def median_filter(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to noisy image (salt & pepper noise expected)
    imagePath = os.path.join(root, 'resources/images/image_with_noise.jpg')
    print(f"Loading image from: {imagePath}")

    # Load original image in BGR format
    image = cv.imread(imagePath)
    imageInRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # For matplotlib (unused here)

    # **CREATE SYNTHETIC SALT-AND-PEPPER NOISE** on image copy
    noisyImage = image.copy()  # Work on duplicate to preserve original
    noiseProbability = 0.05    # 5% of pixels will be noisy
    
    # Generate random noise map same size as image (H, W) - ignores channels
    noise = np.random.rand(noisyImage.shape[0], noisyImage.shape[1])
    
    # **SALT NOISE**: Set 2.5% pixels to BLACK (0) where noise < 0.025
    noisyImage[noise < noiseProbability/2] = 0 
    
    # **PEPPER NOISE**: Set 2.5% pixels to WHITE (255) where noise > 0.975
    noisyImage[noise > 1 - noiseProbability] = 255 

    # **MEDIAN FILTER**: Removes salt-and-pepper noise using 5x5 kernel
    # Replaces each pixel with MEDIAN of its 25 neighbors (highly effective for impulse noise)
    imageFilter = cv.medianBlur(noisyImage, 5)  # Kernel size MUST be odd

    # **2-IMAGE COMPARISON**
    plt.figure(figsize=(12, 5))
    plt.subplot(121)  # 1x2 grid, left position
    plt.imshow(cv.cvtColor(noisyImage, cv.COLOR_BGR2RGB))  # FIX: Convert BGR→RGB
    plt.title('Noisy Image (5% salt+pepper)')
    plt.axis('off')
    
    plt.subplot(122)  # Right position
    plt.imshow(cv.cvtColor(imageFilter, cv.COLOR_BGR2RGB))  # FIX: Convert BGR→RGB
    plt.title('Median Filter (5x5 kernel)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    median_filter()
