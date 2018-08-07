import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
for file in os.listdir("masks"):
    if file.endswith(".png"):
        img = cv2.imread('masks/'+file,0)
        kernel = np.ones((3,3),np.uint8)
        edges = cv2.Canny(img,100,200)
        dilation = cv2.dilate(edges,kernel,iterations = 1)
        cv2.imwrite("modified/"+file, dilation)