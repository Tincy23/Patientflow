import numpy as np
import cv2
def resize():
    path="Downloads/rose.jpg"
    image=cv2.imread(path)
    array2=cv2.resize(image,(1200,1200))
    cv2.imwrite("Downloads/rose.jpg",array2)
    cv2.imshow("rse", array2)
    cv2.waitKey()
resize()
