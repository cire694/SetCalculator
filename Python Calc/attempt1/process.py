import cv2 as cv
import numpy as np

#credits: https://github.com/dharm1k987/Card_Recognizer/blob/master/current/process.py
def approx(contour):
    epsilon = 0.1 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)

    return len(approx), approx

def findContours(img, grayscale, draw=False):
    
    contours, _ = cv.findContours(grayscale, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv.contourArea, reverse=True)
    
    
    
    area_filtered_contour = []
    for contour in contours:
        numSides, approx_shape = approx(contour)

        if cv.contourArea(contour) > 10000 and numSides == 4:

            area_filtered_contour.append(contour)

            x, y, w, h = cv.boundingRect(approx_shape)

            if draw:
                cv.rectangle(img, (x, y), (x + w, y+h), (0, 255, 0), 10)
            
            #storing the corners as [[x, y]]
            l1 = np.array(approx_shape[0]).tolist()
            l2 = np.array(approx_shape[1]).tolist()
            l3 = np.array(approx_shape[2]).tolist()
            l4 = np.array(approx_shape[3]).tolist()

            #sorting: top left, bot left, top right, bot right
            sorted_corners = []
            #first sort by x value
            sortX = sorted([l1, l2, l3, l4], key = lambda x : x[0][0])
            #put the left side first
            sorted_corners.extend(sorted(sortX[0:2], key = lambda x : x[0][1], reverse=True)) #coordinates 
            #now sort the right side
            sorted_corners.extend(sorted(sortX[2:4], key = lambda x : x[0][1], reverse=True))

            area_filtered_contour.extend(sorted_corners)

            #circling the corners
            if draw:
                for corner in sorted_corners:
                    cv.circle(img, (corner[0][0], corner[0][1]), 10, (0, 0, 255), 3)


    return area_filtered_contour    

def findContours2(img, original, draw=False):
    # find the set of contours on the threshed image
    contours, hier = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # sort them by highest area
    proper = sorted(contours, key=cv.contourArea, reverse=True)

    four_corners_set = []

    for cnt in proper:
        area = cv.contourArea(cnt)
        perimeter = cv.arcLength(cnt, closed=True)

        # only select those contours with a good area
        if area > 10000:
            # find out the number of corners
            approx = cv.approxPolyDP(cnt, 0.01 * perimeter, closed=True)
            numCorners = len(approx)

            if numCorners == 4:
                # create bounding box around shape
                x, y, w, h = cv.boundingRect(approx)

                if draw:
                    cv.rectangle(original, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # make sure the image is oriented right: top left, bot left, bot right, top right
                l1 = np.array(approx[0]).tolist()
                l2 = np.array(approx[1]).tolist()
                l3 = np.array(approx[2]).tolist()
                l4 = np.array(approx[3]).tolist()

                finalOrder = []

                # sort by X vlaue
                sortedX = sorted([l1, l2, l3, l4], key=lambda x: x[0][0])

                # sortedX[0] and sortedX[1] are the left half
                finalOrder.extend(sorted(sortedX[0:2], key=lambda x: x[0][1]))

                # now sortedX[1] and sortedX[2] are the right half
                # the one with the larger y value goes first
                finalOrder.extend(sorted(sortedX[2:4], key=lambda x: x[0][1], reverse=True))

                four_corners_set.append(finalOrder)

                if draw:
                    for a in approx:
                        cv.circle(original, (a[0][0], a[0][1]), 10, (255, 0, 0), 3)

    return four_corners_set
