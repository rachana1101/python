import cv2 as cv      # OpenCV for BGR image loading and channel operations
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for subplot grid display
import numpy as np    # NumPy for array matching with zeros_like()

def median_filter(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux path separators)
    imagePath = os.path.join(root, 'resources/images/image_with_noise.jpg')
    print(f"Loading image from: {imagePath}")

    image = cv.imread(imagePath)
    imageInRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # Convert BGR→RGB for Matplotlib (unused here)

    noisyImage = image.copy()
    noiseProbability  = 0.05 
    noise = np.random.rand(noisyImage.shap[0], noisyImage.shape[1])
    noisyImage[noise < noiseProbability/2] = 0 
    noisyImage[noise > 1 - noiseProbability] = 255 

    imageFilter = cv.medianBlur(noisyImage, 5)

    plt.figure()
    plt.subplot(121)
    plt.imshow(noisyImage)
    plt.subplot(122)
    plt.imshow(imageFilter)

    plt.show()

if __name__ == '__main__':
    median_filter()