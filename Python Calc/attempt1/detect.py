import cv2 as cv
import numpy as np
import attempt1.process as process

cap = cv.VideoCapture(0)
# 1) convert to RBG by thresholding 
# 2) some sort of calibration matrix?
# 3) cv.findContours
# 4) 

while True:
    ret, frame = cap.read()
    if not ret:
        print("image not found")
        break

    grayscale_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    