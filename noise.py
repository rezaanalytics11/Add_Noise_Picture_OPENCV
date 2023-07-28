import numpy as np
import os
import cv2
def noisy(a,file_name):
   image=cv2.imread(rf'C:\Users\Ariya Rayaneh\Desktop\{file_name}')
   if a==1:
      #noise_typ == "gauss"
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss

      cv2.imshow('output', noisy)
      cv2.imwrite(rf'C:\Users\Ariya Rayaneh\Desktop\picture_noise_gauss{file_name}.png', noisy)
      cv2.waitKey()

   elif a==2:
      #noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.004
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1
      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0

      cv2.imshow('output', out)
      cv2.imwrite(rf'C:\Users\Ariya Rayaneh\Desktop\picture_noise_s&p{file_name}.png', out)
      cv2.waitKey()

   elif a==3:
      #noise_typ == "poisson":
      vals = len(np.unique(image))
      vals = 2 ** np.ceil(np.log2(vals))
      noisy = np.random.poisson(image * vals) / float(vals)

      cv2.imshow('output', noisy)
      cv2.imwrite(rf'C:\Users\Ariya Rayaneh\Desktop\picture_noise_poisson{file_name}.png', noisy)
      cv2.waitKey()

   elif a==4:
      #noise_typ =="speckle":
      row,col,ch = image.shape
      gauss = np.random.randn(row,col,ch)
      gauss = gauss.reshape(row,col,ch)
      noisy = image + image * gauss

      cv2.imshow('output', noisy)
      cv2.imwrite(rf'C:\Users\Ariya Rayaneh\Desktop\picture_noise_speckle{file_name}.png', noisy)
      cv2.waitKey()


a=int(input('Please input the noise type(4 for "speckle",3 for "poisson",2 for "s&p",1 for "gauss"): '))
file_name=input('Please insert the file name(e.g obama.jpg): ')

noisy(a,file_name)


