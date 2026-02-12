import cv2 as cv      # OpenCV for BGR image loading and channel operations
import os             # OS module for building file paths safely
import matplotlib.pyplot as plt  # Matplotlib for subplot grid display
import numpy as np    # NumPy for array matching with zeros_like()

def guassian_kernel(size, sigma): 
    kernel = cv.getGaissianKernel(size, sigma)
    kernel = np.outer(kernel, kernel)
    return kernel

def gaussian_filter(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux path separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    image = cv.imread(imagePath)
    #imageInRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # Convert BGR→RGB for Matplotlib (unused here)

    n = 51 
    figure = plt.figure()
    plt.subplot(121)
    kernel = guassian_kernel(n,8)
    plt.show(kernel)

    ax = figure.add_subplot(122, projection='3d')
    x = np.arrange(0, n, 1)
    y = np.arrange(0, n, 1)

    X,Y = np.meshgrid(x,y)    
    ax.plot_surface(X,Y, kernel, cmap='viridis')

    plt.show()

if __name__ == '__main__':
    gaussian_filter()