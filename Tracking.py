import numpy as np
import cv2
#import tr

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')


def Threshold(point,min,max):
    if point < min:
        return "Left"
    elif min < point < max:
        return "Centre"
    elif point > max:
        return "Right"
#number signifies camera
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray)
    for (ex,ey,ew,eh) in eyes:
        #print(ex,ey,ew,eh)
        a=int(ew/3)
        b=int(eh/3)
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.line(img, (ex+a,ey), ((ex+a,ey+eh)), (0,0,255),1)   #draw cross
        cv2.line(img, (ex+2*a,ey), ((ex+2*a,ey+eh)), (0,0,255),1)   #draw cross
        cv2.line(img, (ex,ey+b), ((ex+ew,ey+b)), (0,0,255),1)
        cv2.line(img, (ex,ey+2*b), ((ex+ew,ey+2*b)), (0,0,255),1)   #draw cross
        #cv2.line(img, (ex+ew,ey), ((ex,ey+eh)), (0,0,255),1)
        roi_gray2 = gray[ey:ey+eh, ex:ex+ew]
        roi_color2 = img[ey:ey+eh, ex:ex+ew]
        circles = cv2.HoughCircles(roi_gray2,cv2.HOUGH_GRADIENT,1,200,param1=200,param2=1,minRadius=10,maxRadius=10)
        try:
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(roi_color2,(i[0],i[1]),i[2],(255,255,255),1)
                #print("drawing circle", i[0].astype("int"),i[1].astype("int"))
                # draw the center of the circle
                cv2.circle(roi_color2,(i[0],i[1]),1,(255,255,255),1)
                k=Threshold(i[1],35,45)
                print(i[1],k)
                #tr.transmit_code(k)
        except Exception as e:
            print(e)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
