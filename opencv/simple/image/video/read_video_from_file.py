import cv2 as cv
import os  


def read_video():
        root = os.getcwd()
        videoPath = os.path.join(root, '../../Downloads', 'forest.mp4')
        print(videoPath)

        capture = cv.VideoCapture(videoPath)

        while capture.isOpened(): 
              ret, frame = capture.read()
              cv.imshow('video', frame)
              delay = int(1000/60)

              #wait till the key is hit 
              if cv.waitKey(delay) == ord('q'): 
                    break

if __name__ == "__main__":
    read_video() 



