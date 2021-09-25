import cv2 #imported Opencv library
cam = cv2.VideoCapture(0)
# while camera open, read camera
while cam.isOpened():
    ret, frame = cam.read()
    # if the 'A' is pressed wait 10 milliseconds then destroy window
    if cv2.waitKey(10) == ord('a'):
        break
    cv2.imshow('Security cam', frame)
