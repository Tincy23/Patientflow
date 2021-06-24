import cv2
def imagecapture():
    Video1=cv2.VideoCapture(0)
    cascade1=cv2.CascadeClassifier('')
    while(True):
        frame1=Video1.read()
        face=cascade1.detectMultiScale(frame1[1])
        print(face)
        #print(frame1[1])
        #cv2.imshow("video",face[0])
        #if(cv2.waitKey(1)==ord('a')):
           # break
        #cv2.waitKey(0)
        #print(len(frame1))
imagecapture()
