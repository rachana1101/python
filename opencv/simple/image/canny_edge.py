import cv2 as cv      # OpenCV for image I/O, resizing, and Canny edge detection
import os             # OS module for cross-platform file paths
import matplotlib.pyplot as plt  # Matplotlib for image preview (unused here)

# **EMPTY CALLBACK**: Required for trackbar creation (never called)
def callback(arg): 
    pass

def canny_edge(): 
    root = os.getcwd()  # Gets current working directory (script location)
    
    # Build full path to image file (handles Windows/Linux/Mac separators)
    imagePath = os.path.join(root, 'resources/images/cutecat.jpg')
    print(f"Loading image from: {imagePath}")

    # Load color image (BGR format) → convert to RGB (matplotlib expects RGB)
    image = cv.imread(imagePath)
    if image is None:
        print("ERROR: Image not found!")
        return
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # Store RGB version for preview

    # Optional resize (scale=1 keeps original size)
    height, width, _ = image.shape
    scale = 1  # Change to 0.5 for half-size (faster processing)
    heightScale = int(height * scale)
    widthScale = int(width * scale)
    img = cv.resize(image_rgb, (widthScale, heightScale), interpolation=cv.INTER_LINEAR)

    # **CREATE INTERACTIVE WINDOW**
    win_name = 'Canny Edge Detector'  # Window title
    cv.namedWindow(win_name)         # Create resizable window
    
    # **CREATE TRACKBARS**: Adjust Canny thresholds interactively
    cv.createTrackbar('Min Threshold', win_name, 50, 255, callback)  # Default=50
    cv.createTrackbar('Max Threshold', win_name, 150, 255, callback) # Default=150

    # **MAIN LOOP**: Real-time edge detection until 'q' pressed
    while True: 
        # **EXIT CONDITION**: Press 'q' to quit
        if cv.waitKey(1) & 0xFF == ord('q'): 
            break

        # **READ TRACKBAR VALUES** (0-255 range)
        minThres = cv.getTrackbarPos('Min Threshold', win_name)
        maxThres = cv.getTrackbarPos('Max Threshold', win_name)

        # **CANNY EDGE DETECTION**:
        # - Low threshold: Weak edges (connectivity)
        # - High threshold: Strong edges (primary)
        # Algorithm auto-links weak→strong edges
        canny_edge = cv.Canny(img, minThres, maxThres, apertureSize=3)

        # **DISPLAY EDGES** in real-time (white=edges, black=no edges)
        cv.imshow(win_name, canny_edge)

    cv.destroyAllWindows()  # Close all OpenCV windows cleanly

if __name__ == '__main__': 
    canny_edge()
