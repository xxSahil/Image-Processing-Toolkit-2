# ============================================================
# Assignment 2 
# Task 1
#
# Name: Sahil Minhas
# Student ID: 180709550
# Date: Nov 9, 2025
#
# ============================================================

import cv2
import numpy as np

# Set relative paths
INPUT_PATH = "Images/img1.tif"
OUTPUT_MARR = "Output Images/img1_marr_hildreth.tif"
OUTPUT_CANNY = "Output Images/img1_canny.tif"


#read input img
img = cv2.imread(INPUT_PATH, cv2.IMREAD_GRAYSCALE)

# Marr-Hildreth Implementation
sigma = 1.4 #best average value to remove small noise and keep major edges
kernel = (9, 9) # using recommended value kernel = 6 * sigma + 1, so round to 9
blurred_img = cv2.GaussianBlur(img, kernel, sigma)

laplacian = cv2.Laplacian(blurred_img, cv2.CV_64F)

def zero_crossing(lap_img):
    zero_cross = np.zeros_like(lap_img, dtype=np.uint8) #Blank img for storing edges
    rows, cols = lap_img.shape

    #Loop through range excluding borders
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            square = lap_img[i - 1: i + 2, j - 1: j + 2] #3x3 sqaure around the pixel
            square_min, square_max = square.min(), square.max()

            if square_min < 0 < square_max:
                zero_cross[i, j] = 255 #Mark edge
    
    return zero_cross


edges_marr = zero_crossing(laplacian)

cv2.imwrite(OUTPUT_MARR, edges_marr)

#Canny Edge

edges_canny = cv2.Canny(img, 50, 150)
cv2.imwrite(OUTPUT_CANNY, edges_canny)




