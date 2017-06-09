# IMPORTING REQUIRED MODULES
import cv2
import numpy as np
import serial
import time

#INITIALSING THE ARDUINO
arduino=serial.Serial('COM24',9600,timeout=0.1) #CHANGE THE COM PORT TO THE PORT YOU HAVE CONNECTED YOUR ARDUINO AND MAKE SURE THE BAUD RATE OF THE ARDUINO AND THE BUAD RATE SPECIFIED HERE ARE THE SAME
time.sleep(2)

#FOR INITIALISING THE CAMERA
cap=cv2.VideoCapture(0) #USE 1 INSTEAD OF 0 FOR EXTERNAL CAMERA

#SETTING DEFAULT VALUES FOR FINDING CONTOURS
x1=y1=0
r1=50
a1=500
tempset=0

#CREATING INFINITE LOOP
while(1):

    #STARTING READING OPERATION
    ret,frame=cap.read()

    #CONVERTING BGR TO HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #SETTING HSV RANGE FOR COLOUR DETECTION
    low_ver1=np.array([110,50,50])
    upp_ver1=np.array([130,255,255])

    #MASKING
    mask1=cv2.inRange(hsv,low_ver1,upp_ver1)

    #KERNELING
    kernel_morpho=np.ones((5,5),np.uint8)

    #REMOVING NOISES
    blur1=cv2.GaussianBlur(mask1,(5,5),0)
    erode1=cv2.erode(blur1,kernel_morpho,iterations=1)
    dil1=cv2.dilate(erode1,kernel_morpho,iterations=1)
    opening1=cv2.morphologyEx(dil1,cv2.MORPH_OPEN,kernel_morpho)
    closing1=cv2.morphologyEx(opening1,cv2.MORPH_CLOSE,kernel_morpho)

    #FOR COMAPRING - SETTING PREVIOUS POSITION AS CENTRE
    if tempset==1:
        centre=centre1 

    #CONTOURS
    ret1,thresh1=cv2.threshold(closing1,127,255,cv2.THRESH_BINARY)
    cnts1=cv2.findContours(thresh1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    centre1=None
    for i in range(0,len(cnts1)):
        area1=cv2.contourArea(cnts1[i])
        if area1 > a1:
            (x1,y1),radius1=cv2.minEnclosingCircle(cnts1[i])
            M1=cv2.moments(cnts1[i])
            centre1=(int(M1['m10']/M1['m00']),int(M1['m01']/M1['m00']))
            if radius1 > r1:
                cv2.circle(frame,centre1,int(radius1),(0,255,0),2)

    #FOR COMPARING - SO THAT IT DOSENT AFFECT THE PURPOSE
    tempset=1

    #ARDUINO
    while True:
        data=arduino.readline()
        if data:
            if data=='Y':
                print "\n INCOMING SIGNAL FROM ARDUINO MEGA...."
                if centre1 > centre :
                    arduino.write('F')
                    time.sleep(2)
                    data=='E'
                    break
                if centre1 < centre:
                    arduino.write('B')
                    time.sleep(2)
                    data=='E'
                    break
                if centre1 == centre:
                    arduino.write('S')
                    time.sleep(2)
                    data=='E'
                    break

        else:
            print " \n NO INCOMING SIGNAL FROM ARDUINO !!!! "
            break



    #DISPLAY
    cv2.imshow('MASKED',mask1)
    cv2.imshow('OBJECT',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

arduino.close()    
cam.release()
cv2.destroyAllWindows()
