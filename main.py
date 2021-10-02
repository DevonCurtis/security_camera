import cv2 #imported Opencv library
cam = cv2.VideoCapture(0)
# while camera open, read camera
while cam.isOpened():
    #Capturing two instances
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    # if the 'A' key is pressed wait 10 milliseconds then destroy window
    if cv2.waitKey(10) == ord('a'):
        break
    cv2.imshow('Security cam', diff)
