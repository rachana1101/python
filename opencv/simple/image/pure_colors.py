# OpenCV BGR array: [[[0, 0, 255]]]  # B=0, G=0, R=255 per pixel
# Matplotlib reads as RGB: R=0, G=0, B=255 → Pure BLUE!

import cv2 as cv  # OpenCV for image channel merging (BGR format)
import os         # OS module for file/path ops (unused here)
import matplotlib.pyplot as plt  # Matplotlib for image display and subplots
import numpy as np  # NumPy for array creation (images as arrays)

def pure_colors(): 
    zeros = np.zeros((100,100))  # 100x100 array of 0s (black channels for G/R)
    
    ones = np.ones((100,100))    # 100x100 array of 1s (base for scaling blue channel)
    
    bImg = cv.merge((zeros, zeros, 255*ones))  # Merges BGR: Blue=zeros*255? No—wait, order is B=zeros(0), G=zeros(0), R=255*ones(255)
                                                # Results in pure blue image (BGR: [0,0,255] per pixel? Actually B=0? Wait no:
                                                # cv.merge((B,G,R)) so B=zeros(0), G=zeros(0), R=255 → pure RED in BGR! Title mismatch.

    gImg = cv.merge((zeros, 255*ones, zeros))  #green 
    rImg = cv.merge((255*ones ,zeros, zeros))  #red
    blackImg = cv.merge((zeros ,zeros, zeros))  #black
    whiteImg = cv.merge((255*ones ,255*ones, 255*ones))  #black


    plt.figure()  # New figure for plotting
    plt.subplot(231)  # 2x3 grid, 1st subplot (room for more colors) # 2: 2 row tall, 3: 3 columns wide 1: selects subplot#1 
    plt.imshow(bImg)  # Shows BGR array (Matplotlib swaps to RGB view: red appears red)
    plt.title('blue') # Title says 'blue' but image is red due to channel order

    plt.subplot(232)  
    plt.imshow(gImg)  
    plt.title('green') 

    plt.subplot(233)  
    plt.imshow(rImg)  
    plt.title('red') 

    plt.subplot(234)  
    plt.imshow(blackImg)  
    plt.title('black') 

    plt.subplot(235)  
    plt.imshow(whiteImg)  
    plt.title('white') 
    

    plt.show()  # Displays the plot

if __name__ == '__main__':
    pure_colors()
