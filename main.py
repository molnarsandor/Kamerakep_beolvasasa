from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

tello.streamon()
while True:
    frame_read = tello.get_frame_read()
    frame = frame_read.frame
    cv2.imshow("Stream", frame)
    cv2.waitKey(100)
