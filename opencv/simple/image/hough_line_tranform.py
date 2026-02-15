# 1. **Edges first**: Canny → binary edge map
# 2. **Vote in ρ-θ space**: Each edge point votes for lines passing through it
# 3. **Peaks = lines**: High-vote (ρ, θ) pairs = detected lines
# 4. **Draw**: Convert (ρ, θ) → 2 endpoints using math above

# **Tune**:
# - threshold ↑: Fewer, stronger lines
# - distResolution ↓: Finer position accuracy

import cv2 as cv      # OpenCV for grayscale processing, Canny, HoughLines
import os             # OS module for cross-platform file paths
import matplotlib.pyplot as plt  # Matplotlib for 2x2 image display
import numpy as np    # NumPy for vector math (line endpoint calculation)

def hough_line_transformation(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux/Mac separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # **LOAD GRAYSCALE**: HoughLines needs single-channel binary edges
    image = cv.imread(imagePath, cv.IMREAD_GRAYSCALE)
    if image is None:  # **FIX**: Move error check HERE
        print("ERROR: Image not found!")
        return

    # **PREPROCESSING PIPELINE**:
    # Gaussian blur removes noise before edge detection (small kernel for details)
    imageBlur = cv.GaussianBlur(image, (5, 5), 3)  # sigma=3 for moderate smoothing

    # Canny edges: Standard preprocessing for Hough (50-150 thresholds typical)
    cannyImage = cv.Canny(imageBlur, 50, 150)

    # **VISUALIZE PIPELINE** (2x2 grid)
    plt.figure(figsize=(12, 10))
    plt.subplot(221); plt.imshow(image, cmap='gray'); plt.title('Original Grayscale'); plt.axis('off')
    plt.subplot(222); plt.imshow(imageBlur, cmap='gray'); plt.title('Gaussian Blur'); plt.axis('off')
    plt.subplot(223); plt.imshow(cannyImage, cmap='gray'); plt.title('Canny Edges'); plt.axis('off')

    # **HOUGH LINE PARAMETERS**:
    distResolution = 1           # ρ precision: 1 pixel
    angleResolution = np.pi / 180  # θ precision: 1 degree (π/180 radians)
    threshold = 50               # Min votes (edge points) to detect line
    lines = cv.HoughLines(cannyImage, distResolution, angleResolution, threshold)
    print(f"Detected {len(lines) if lines is not None else 0} lines: {lines}")

    # **DRAW LINES ON COLOR COPY** (not grayscale!)
    color_image = cv.imread(imagePath)  # Reload original COLOR image
    color_image = cv.cvtColor(color_image, cv.COLOR_BGR2RGB)  # For matplotlib

    k = 1000  # Distance from line center to endpoints (±k along perpendicular)

    if lines is not None:  # **FIX**: Check if lines detected
        for curline in lines: 
            rho, theta = curline[0]  # Extract ρ, θ from [[ρ, θ]]
            
            # **PARAMETRIC LINE EQUATION**: ρ = x*cosθ + y*sinθ
            dhat = np.array([[np.cos(theta)], [np.sin(theta)]])  # Unit normal vector
            d = rho * dhat                                        # Point on line closest to origin
            
            lhat = np.array([[-np.sin(theta)], [np.cos(theta)]])  # Unit line direction vector
            p1 = d + k * lhat  # Endpoint 1: Extend +k along line direction
            p2 = d - k * lhat  # Endpoint 2: Extend -k along line direction
            
            p1 = p1.astype(int)  # Convert to pixel coordinates
            p2 = p2.astype(int)

            # **DRAW LINE**: White (255,255,255), thickness=10 on BGR version
            cv.line(color_image, (p1[0][0], p1[1][0]), (p2[0][0], p2[1][0]), (255, 255, 255), 10)

    # **FINAL RESULT**: Original → Lines overlaid
    plt.subplot(224); plt.imshow(color_image); plt.title('Hough Lines Detected'); plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    hough_line_transformation()
