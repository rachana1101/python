import cv2 as cv
import numpy as np 
import os 

def read_video_from_webcam() : 
    webcam = cv.VideoCapture(0)
    if not webcam.isOpened():
        exit() 

    while True: 
        ret, frame = webcam.read()
        if ret: 
            cv.imshow('Webcame', frame)

        if cv.waitKey(1) == ord('q'): 
            break

    webcam.release()        
    cv.destroyAllWindows()

if __name__ == '__main__': 
    read_video_from_webcam()