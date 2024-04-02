import numpy as py;
import cv2 as cv;

cap = cv.VideoCapture(0)

def aspect_ratio(cnt): #x, y is the coord of top left, w, h is the rectangle
    _, _, w, h = cv.boundingRect(cnt)
    return max(float(w) / h, float(h)/w)


#https://www.kaggle.com/datasets/kwisatzhaderach/set-cards
#https://web.stanford.edu/class/cs231a/prev_projects_2021/CS231A_Project_Progress_Report__1_.pdf
#https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123?gi=6e86a2a69045
# need image segmentation
while True:
 
    ret, frame = cap.read(0)

    if not ret:
        print("unable to capture frame.")
        break

    # card segmentation:

   
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #thresholding the image
    #thresholding is when the pixel is higher than a value, it turns white(indicating foreground), otherwise turns black
    _, thresh = cv.threshold(gray_img, 150, 255, cv.THRESH_BINARY)

    #Find countours
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)#only retreve the contours that form an outline
    contour_img = frame.copy()

    

    filtered_contours = []
    for contour in contours:
        if 1.1 < aspect_ratio(contour) < 1.9:
            epsilon = 0.03 * cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, 0.03 * cv.arcLength(contour, True), True)
            if len(approx) == 4:
                filtered_contours.append(approx)
                
    
    # aspect_filtered_contour = [contour for contour in contours if cv.isContourConvex(contour)]

    cv.drawContours(contour_img, filtered_contours, -1, (0, 255, 0), 10)
    
    cv.imshow("original", frame)
   



    #display the frames
    if cv.waitKey(1) == ord("q"):
        break


cap.release()
cv.destroyAllWindows()    

