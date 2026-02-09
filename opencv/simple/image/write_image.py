import cv2 as cv
import os 
import numpy

def writeImage(): 
    root = os.getcwd() #read the root 
    imgPath = os.path.join(root, 'opencv', 'images', 'color_tuto.jpg')

    outputPath = os.path.join(root, 'opencv', 'images', 'color_tuto_output.jpg')

    print(imgPath)
    print("Exists?", os.path.exists(imgPath))
    img = cv.imread(imgPath)
    if img is None:
        print("❌ Image not found!")
        return
    
    print(outputPath)
    cv.imwrite(outputPath, img)

if __name__ == '__main__': 
    writeImage()    
