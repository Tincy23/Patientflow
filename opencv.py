import cv2
import numpy as np

def opencvdemo():
    path="orchid events.png."
    img=cv2.imread(path)
    print(img)
    for i in range(0,len(img[0])):
        img[300][i]=[600,350,300]
        img[i][200]=[200,650,800]

        #greyscale
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        print(img2)
    cv2.imshow("image 1",img)
    cv2.waitKey()
opencvdemo()

def img():
    array1=np.full((300,300,3),0,dtype=np.uint8)
    print(array1)
    for i in range(50,100):
        array1[i][50]=[0,0,0]
    cv2.imwrite("abc.png",array1)
    cv2.imshow("",array1)
    cv2.waitkey()
img()

