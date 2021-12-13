import cv2
import numpy
img = cv2.imread('123.png')
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobel1=abs(sobelx)+abs(sobely)
sobel=numpy.sqrt(sobelx**2+sobely**2)

cv2.imwrite('3.png',sobel)
cv2.imwrite('4.png',sobel1)