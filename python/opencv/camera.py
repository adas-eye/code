import cv2

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    cv2.imshow('camera', img)
    cv2.waitKey(30)