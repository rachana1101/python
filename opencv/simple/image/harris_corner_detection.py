import cv2 as cv      # OpenCV for image I/O and Harris corner detection
import os             # OS module for cross-platform file paths
import matplotlib.pyplot as plt  # Matplotlib for 2x2 subplot display
import numpy as np    # NumPy for array operations

def harris_corner_detection(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux/Mac separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Load color image (BGR format)
    image = cv.imread(imagePath)
    if image is None:
        print("ERROR: Image not found!")
        return
    
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # For matplotlib display

    # **PREPARE GRAYSCALE**: Harris needs float32 grayscale (0.0-1.0 range internally)
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # Single channel
    image_gray = np.float32(image_gray) / 255.0         # Normalize to 0.0-1.0

    # **PLOT 1**: Show input grayscale image
    plt.figure(figsize=(12, 10))
    plt.subplot(221)
    plt.imshow(image_gray, cmap='gray')
    plt.title('1. Input Grayscale (float32)')
    plt.axis('off')

    # **HARRIS CORNER DETECTION PARAMETERS**:
    # - block_size=5: Neighborhood size for derivative calculation
    # - sobel_size=3: Sobel kernel for gradient computation  
    # - k=0.04: Sensitivity factor (0.04-0.06 typical)
    block_size = 5
    sobel_size = 3 
    k = 0.04
    harris = cv.cornerHarris(image_gray, block_size, sobel_size, k)

    # **PLOT 2**: Raw Harris response map (bright=strong corners)
    plt.subplot(222)
    plt.imshow(np.log(harris), cmap='jet')  # Log scale + jet colormap for visibility
    plt.title('2. Harris Response Map\n(bright = strong corners)')
    plt.colorbar()
    plt.axis('off')

    # **THRESHOLD & MARK CORNERS** on color image
    harris_threshold = 0.01 * harris.max()  # Dynamic threshold (1% of max response)
    corners = harris > harris_threshold     # Binary corner map
    
    # **PLOT 3**: Binary corner locations
    plt.subplot(223)
    plt.imshow(corners, cmap='gray')
    plt.title(f'3. Corners (threshold={harris_threshold:.3f})')
    plt.axis('off')

    # **PLOT 4**: Original + RED corner markers
    result = image_rgb.copy()
    result[corners > 0] = [255, 0, 0]  # Mark corners RED
    
    plt.subplot(224)
    plt.imshow(result)
    plt.title('4. Original + Detected Corners (RED)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

    print(f"Detected {np.sum(corners)} corners")

if __name__ == '__main__': 
    harris_corner_detection()
