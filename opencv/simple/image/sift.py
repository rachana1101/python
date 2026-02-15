import cv2 as cv      # OpenCV for SIFT feature detection and keypoint visualization
import os             # OS module for cross-platform file paths
import matplotlib.pyplot as plt  # Matplotlib for image display
import numpy as np    # NumPy for array operations

def sift(): 
    """
    **SIFT (Scale-Invariant Feature Transform)**:
    Detects and describes local image features invariant to:
    - Scale changes (zoom in/out)
    - Rotation (image turned)
    - Illumination (light/shadow)
    
    Each keypoint = (x, y, scale, orientation) + 128D descriptor
    Used for: panorama stitching, object recognition, 3D matching
    """
    root = os.getcwd()  # Gets current working directory
    
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # **SIFT NEEDS GRAYSCALE**: Single-channel input only
    image = cv.imread(imagePath, cv.IMREAD_GRAYSCALE)
    if image is None:
        print("ERROR: Image not found!")
        return

    # **CREATE SIFT DETECTOR**: OpenCV's implementation (patent-free since 2020)
    sift = cv.SIFT_create()
    
    # **DETECT**: Finds keypoints across all scales/orientations
    keypoints = sift.detect(image, None)  # None = no mask (full image)
    
    print(f"✅ Detected {len(keypoints)} SIFT keypoints")

    # **VISUALIZE**: Rich keypoints show scale (circle size) + orientation (lines)
    image_kp = cv.drawKeypoints(
        image, 
        keypoints, 
        image,  # Output image
        flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS  # Show size/orientation
    )

    plt.figure(figsize=(12, 8))
    plt.imshow(image_kp, cmap='gray')
    plt.title(f'SIFT Keypoints ({len(keypoints)} detected)\n'
              f'🔴 Circle size = scale | Line = orientation')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    # **KEYPOINT DETAILS** (first 3 examples)
    print("\n📍 Sample keypoints (x, y, size, angle°):")
    for i, kp in enumerate(keypoints[:3]):
        print(f"  {i+1}. ({kp.pt[0]:.0f}, {kp.pt[1]:.0f})  size={kp.size:.1f}  "
              f"angle={kp.angle:.0f}°")

if __name__ == '__main__': 
    sift()
