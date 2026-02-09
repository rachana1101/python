import cv2 as cv
import os 
import numpy

def readImage(): 
    root = os.getcwd() #read the root 
    imgPath = os.path.join(root, 'opencv', 'images', 'color_tuto.png')
    print(imgPath)
    print("Exists?", os.path.exists(imgPath))

    img = cv.imread(imgPath)
    if img is None:
        print("❌ Image not found!")
        return

    cv.imshow('Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__': 
    readImage()    
