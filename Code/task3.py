# =============================
# Assignment 2 - CP467
# Task 3
#
# Name: Sahil Minhas
# Student ID: 180709550
# Date: Nov 9, 2025
#
# ===========================

import cv2
import numpy as np

OUTPUT_PATH = "Output Images/"

for i in range(1, 6):
    img_name = f"Images/eye{i}.tif"
    img = cv2.imread(img_name)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 2)

    edges = cv2.Canny(blurred, 50, 150)

    iris = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,
                            dp = 1, minDist = 50, 
                            param1=100, param2=30,
                            minRadius=80, maxRadius=130)
    
    pupil = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                             param1=100, param2=15,
                             minRadius=20, maxRadius=60)

    output_img = img.copy()
    
    if pupil is not None:
        pupil = np.uint16(np.around(pupil))
        for (x, y, r) in pupil[0, :1]:
            cv2.circle(output_img, (x, y), r, (0, 255, 0), 2) #circle
            cv2.circle(output_img, (x, y), 2, (0, 0, 255), 3) #Dot

    if iris is not None:
        iris = np.uint16(np.around(iris))
        for (x, y, r) in iris[0, :1]:
            cv2.circle(output_img, (x, y), r, (255, 0, 0), 2) #Circle
            cv2.circle(output_img, (x,y), 2, (0, 0, 255), 3) #Dot

    cv2.imwrite(OUTPUT_PATH + f"eye{i}_edges.tif", edges)
    cv2.imwrite(OUTPUT_PATH + f"eye{i}_circles.tif", output_img)


