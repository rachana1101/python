# Gaussian blur is convolution—specifically, it's convolution using a Gaussian-shaped kernel rather than a uniform one like your first averaging code.
# Convolution = General math operation (slide kernel → weighted sum)
# Gaussian blur = Convolution where kernel = Gaussian function (bell curve weights)
# | General Convolution (cv.filter2D)        | Gaussian Blur (cv.GaussianBlur)               |
# | ---------------------------------------- | --------------------------------------------- |
# | Any kernel shape (box, edge, sharpen...) | Always Gaussian kernel shape                  |
# | kernel = np.ones((n,n))/(n*n) (flat)     | kernel = bell curve (center high, edges fade) |
# | Uniform neighborhood average             | Weighted: nearby pixels matter more           |
#
# Gaussian blur = "fancy convolution with smooth weights." Your sigma slider just changes how wide the bell curve spreads.
#
import cv2 as cv      # OpenCV for BGR image loading and Gaussian filtering operations
import os             # OS module for building platform-safe file paths
import matplotlib.pyplot as plt  # Matplotlib for subplot visualization (2D/3D kernel plots)
import numpy as np    # NumPy for array operations and meshgrid creation

# Empty callback function required for OpenCV trackbars (does nothing, just placeholder)
def callback(input):
    pass 

# Creates a 2D Gaussian kernel from 1D kernels using outer product
def guassian_kernel(size, sigma): 
    # cv.getGaussianKernel returns a 1D vertical Gaussian kernel (column vector)
    kernel = cv.getGaussianKernel(size, sigma)
    # np.outer(kernel, kernel) creates 2D kernel: vertical × horizontal = separable 2D Gaussian
    # This is mathematically equivalent to full 2D Gaussian but more efficient
    kernel = np.outer(kernel, kernel)
    return kernel

def gaussian_filter(): 
    # Get current working directory where script is running
    root = os.getcwd()
    
    # Build cross-platform path to cutecat.jpg (works on Windows/Linux/Mac)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Load image in BGR format (OpenCV default) - no RGB conversion needed for filtering
    image = cv.imread(imagePath)
    #imageInRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # Commented out: unused here

    # Kernel size = 51x51 pixels (odd number required for symmetric convolution)
    n = 75
    
    # Create figure with subplots to visualize the Gaussian kernel
    figure = plt.figure()
    
    # Left subplot (121 = 1 row, 2 columns, subplot 1): 2D heatmap of kernel
    plt.subplot(121)
    kernel = guassian_kernel(n, 8)  # sigma=8 creates smooth, wide Gaussian
    plt.imshow(kernel, cmap='hot')  # Visualize kernel weights as heatmap
    plt.title('2D Gaussian Kernel')  # Bright center = high weights, dark edges = low weights

    # Right subplot (122): 3D surface plot of same kernel
    ax = figure.add_subplot(122, projection='3d')  # 3D axes for surface plot
    x = np.arange(0, n, 1)  # X coordinates: 0,1,2,...,50
    y = np.arange(0, n, 1)  # Y coordinates: 0,1,2,...,50

    # Create 2D coordinate grid for surface plotting
    X, Y = np.meshgrid(x, y)    
    
    # Plot kernel as 3D surface (bell shape): center peak, smooth dropoff
    ax.plot_surface(X, Y, kernel, cmap='viridis')
    ax.set_title('3D Gaussian Kernel Surface')

    # Show kernel visualization (matplotlib window pops up)
    plt.show()

    # Create interactive OpenCV window for real-time Gaussian blur demo
    winName = 'gaus filter'
    cv.namedWindow(winName)  # Create resizable window
    
    # Create trackbar slider labeled "sigma" (range 1-20, starts at 1)
    # callback() called when slider moves (does nothing in this case)
    cv.createTrackbar('sigma', winName, 1, 20, callback)
    
    # Get original image dimensions
    height, width, _ = image.shape
    scale = 1/4  # Reduce to 25% size for faster preview
    width = int(width * scale)
    height = int(height * scale)

    # Resize image for faster trackbar interaction (smaller = more responsive)
    image = cv.resize(image, (width, height))

    # Main interactive loop: update blur in real-time as you drag slider
    while True: 
        # Exit loop when 'q' key pressed (1ms key check delay)
        if cv.waitKey(1) == ord('q'):
            break

        # Read current sigma value from trackbar (1-20)
        sigma = cv.getTrackbarPos('sigma', winName)
        
        # Apply Gaussian blur: (n,n) kernel size, sigma controls blur strength
        # Higher sigma = wider blur (more pixels influence center pixel)
        imageFilter = cv.GaussianBlur(image, (n, n), sigma)
        
        # Display blurred image in OpenCV window (updates ~30fps)
        cv.imshow(winName, imageFilter)

    # Clean up: close all OpenCV windows when 'q' pressed
    cv.destroyAllWindows()    

# Standard Python idiom: run function only when script executed directly
if __name__ == '__main__':
    gaussian_filter()
