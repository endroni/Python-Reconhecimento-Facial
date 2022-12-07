import cv2 

webCam = cv2.VideoCapture(0)

if webCam.isOpened():
    print(webCam.read())

