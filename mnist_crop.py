import cv2

image=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\mnist.jpg')
image=cv2.resize(image,(0,0),fx=2,fy=2)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
crop=image
w,h=image.shape

W_divide=3
H_divide=3
k=[]
for i in range(3):
    for j in range(3):

      image[i*w//3:i*w//3+w//3,j*h//3:j*h//3+h//3]
      crop=image[i*w//3:i*w//3+w//3,j*h//3:j*h//3+h//3]



      cv2.imshow('output',crop)
      cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\crop\picture'+str(i)+str(j)+'.png',crop)
      cv2.waitKey()
