import cv2
import matplotlib.pyplot as plt
image=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\coins.jpg')
image=cv2.resize(image,(0,0),fx=4,fy=4)
_,image=cv2.threshold(image,220,255,cv2.THRESH_BINARY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i,j]>=0 and image[i,j]!=255:
           image[i, j]=0

image=255-image

contours,_=cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for c in contours:
    if len(c)>200:
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(image,(x,y),(x+w,y+h),(150,150,150),4)

#plt.imshow(image,cmap='gray')
cv2.imshow('output',image)
cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\picture_assign_27.png',image)
cv2.waitKey()