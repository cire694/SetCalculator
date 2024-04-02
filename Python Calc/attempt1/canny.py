import numpy as np;
import cv2 as cv;
import attempt1.process as process;

cap = cv.VideoCapture(0)

def aspect_ratio(cnt): #x, y is the coord of top left, w, h is the rectangle
    _, _, w, h = cv.boundingRect(cnt)
    return max(float(w) / h, float(h)/w)

def count_vertices(contour):
    epsilon = 0.1 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)

    return len(approx)


#https://www.kaggle.com/datasets/kwisatzhaderach/set-cards
#https://web.stanford.edu/class/cs231a/prev_projects_2021/CS231A_Project_Progress_Report__1_.pdf
#https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123?gi=6e86a2a69045
while True:
 
    ret, frame = cap.read(0)

    if not ret:
        print("unable to capture frame.")
        break


   
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    blurred = cv.GaussianBlur(gray_img, (11, 11), 0)


    contour_img = frame.copy()

    edges = cv.Canny(blurred, 50, 150)
    
    # making the contours more continous
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    edges = cv.dilate(edges, kernel, iterations = 1)


    adaptivea_thresh = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 6)
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    quad_filter = []
    for contour in contours:
        if count_vertices(contour) == 4 and abs(aspect_ratio(contour)) > 1.3:
            quad_filter.append(contour)

    cv.drawContours(contour_img, quad_filter, -1, (0, 255, 0), 10)

    

    # cv.imshow("Canny ", contour_img)
    # cv.imshow('processv2', process.findContours(frame, True))
    # cv.imshow('grayscale', edges)
    processed_img = process.findContours2(contour_img, frame, True)
    # print(len(processed_img))
    cv.imshow('process', frame)

    
    # print(len(quad_filter))
    
    
    
    if cv.waitKey(1) == ord("q"):
        break


cap.release()
cv.destroyAllWindows()    

# note to self: solid card's shapes are being detected