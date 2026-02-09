import cv2 as cv
import os

def write_video_to_file():
    webcam = cv.VideoCapture(0, cv.CAP_AVFOUNDATION)
    
    if not webcam.isOpened():
        print("Error: Webcam unavailable.")
        return

    width = int(webcam.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(webcam.get(cv.CAP_PROP_FRAME_HEIGHT))
    print(f"Resolution: {width}x{height}")

    root = os.getcwd()
    video_output_path = os.path.join(root, 'demoVideo.mp4')
    print(video_output_path)

# fourcc = cv.VideoWriter_fourcc(*'avc1') creates a 4-byte integer code identifying the H.264 video codec for your macOS video writer.

# Breakdown

# FourCC = "Four Character Code" - a 4-byte identifier for video codecs (like ZIP for compression).

# cv.VideoWriter_fourcc() packs 4 characters into a 32-bit integer

# *'avc1' unpacks string 'avc1' into 4 separate chars: ('a', 'v', 'c', '1')

# Result: integer 0x31637661 (little-endian byte order: 61 76 63 31)

    fourcc = cv.VideoWriter_fourcc(*'avc1')  # ✅ macOS H.264 - works reliably
    out = cv.VideoWriter(video_output_path, fourcc, 20.0, (width, height))
    
    if not out.isOpened():
        print("Error: VideoWriter still failed.")
        webcam.release()
        return

    while True:
        ret, frame = webcam.read()
        if ret:
            out.write(frame)
            cv.imshow('Webcam', frame)
        else:
            print("Frame read failed.")
            break

        if cv.waitKey(1) == ord('q'):
            break

    webcam.release()
    out.release()
    cv.destroyAllWindows()
    print("✅ Video saved!")

if __name__ == '__main__':
    write_video_to_file()
