# =============================
# Assignment 2 - CP467
# Task 2
#
# Name: Sahil Minhas
# Student ID: 180709550
# Date: Nov 9, 2025
#
# ===========================

import cv2
import numpy as np
from collections import deque

OUTPUT_PATH = "Output Images"

def connected_components(edge_img):
    rows, cols = edge_img.shape
    labels = np.zeros((rows, cols), dtype=np.int32)
    curlab = 1 #Current label

    #8 Neighbours
    neighbours = [(-1,-1), (-1, 0), (-1, 1), 
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    for i in range(rows):
        for j in range(cols):
            #New region
            if labels[i, j] == 0 and edge_img[i, j] == 255:
                labels[i, j] = curlab
                queue = deque([(i, j)])
            
                while queue:
                    curr_x, curr_y = queue.popleft()
                    
                    #Check all neighbours
                    for dir_x, dir_y in neighbours:
                        nbr_x, nbr_y = curr_x + dir_x, curr_y + dir_y

                        #Make sure neighbour is in image
                        if 0 <= nbr_x < rows and 0 <= nbr_y < cols:
                            #Label edge 
                            if edge_img[nbr_x, nbr_y] == 255 and labels[nbr_x, nbr_y] == 0:
                                labels[nbr_x, nbr_y] = curlab
                                queue.append((nbr_x, nbr_y))
                curlab += 1
    return labels    

def colour_random(labels):
    colored = np.zeros((labels.shape[0], labels.shape[1], 3), np.uint8)
    np.random.seed(0)
    for i in range(1, labels.max() + 1):
        colored[labels == i] = np.random.randint(0, 255, 3)
    return colored


#Img creation

edge_marr = cv2.imread(OUTPUT_PATH + "/img1_marr_hildreth.tif", 0)
edge_canny = cv2.imread(OUTPUT_PATH + "/img1_canny.tif", 0)

labels_marr = connected_components(edge_marr)
labels_canny = connected_components(edge_canny)

colour_marr = colour_random(labels_marr)
colour_canny = colour_random(labels_canny)

cv2.imwrite(OUTPUT_PATH + "/img1_connected_marr_hildreth.tif", colour_marr)
cv2.imwrite(OUTPUT_PATH + "/img1_connected_canny.tif", colour_canny)







