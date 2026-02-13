import cv2 as cv      # OpenCV for loading images and applying filters
import os             # OS module for building platform‑safe file paths
import matplotlib.pyplot as plt  # Matplotlib for plotting images
import numpy as np    # NumPy for array operations (not used directly here but often needed)



# Increasing n makes the image more blurry.
# Decreasing n (for the same averaging‑kernel idea) makes it less blurry.

# Why that happens

# Your kernel is an averaging box filter:
# kernel = 1 n 2⋅1 / n×n
# kernel= n 2 1⋅1 n×n.

# A larger n means each output pixel takes an average over a wider neighborhood of pixels → more local details are “smoothed out” → stronger blur.
# A smaller n means each output pixel depends on a tighter neighborhood → less averaging → the result looks closer to the original (less blur).
# For example:
# n = 3 → mild blur.
# n = 10 → noticeable blur.
# n = 100 (as in your code) → very strong, almost “patchy” blur.
# So to decrease blurring: use a smaller n; to increase it: use a larger n.

def convolution_2d(): 
    # Get the current working directory (where the script is located)
    root = os.getcwd()
    
    # Build the full path to the image file: resources/images/cutecat.jpg
    # os.path.join handles forward/backward slashes on any OS
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Load the image from disk into a NumPy array (in BGR format)
    image = cv.imread(imagePath)
    
    # Convert from BGR (OpenCV default) to RGB for correct display in matplotlib
    imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Define the size of the convolution kernel (100x100)
    n = 50
    
    # Create a uniform averaging kernel: all elements = 1.0
    # Divide by n*n so that each output pixel is the average of its neighborhood
    # creates 50X50 matrix 
    kernel = np.ones((n,n), np.float32) / (n*n)
    
    # Apply 2D convolution (image filtering) with the kernel
    # -1 means output depth matches input depth; result is a blurred image
    imgFilter = cv.filter2D(imageRGB, -1, kernel)

    # Create a new matplotlib figure for display
    plt.figure()
    
    # First subplot: show the original RGB image (lighter, sharper)
    plt.subplot(121)
    plt.imshow(imageRGB)

    # Second subplot: show the convolved (blurred) image
    plt.subplot(122)
    plt.imshow(imgFilter)

    # Display the figure window with both images side by side
    plt.show()



# This block runs the function only when the script is executed directly
if __name__ == '__main__':
    convolution_2d()
