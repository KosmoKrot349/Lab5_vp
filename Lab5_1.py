import cv2,copy
import numpy as np
import os
from math import sqrt
img = cv2.imread('123.png')
img[img==255]=254
img2=copy.deepcopy(img)
img3=copy.deepcopy(img2)
for i in range(0,img2.shape[0]):
  for j in range(0,img2.shape[1]):
    jj=j
    ii=i
    if jj==img2.shape[1]-1: jj=-1
    if ii==img2.shape[0]-1: ii=-1
    tlist=[]
    colorij=[img2[i-1,j-1],img2[i-1,j],img2[i-1,jj+1],img2[i,j-1],img2[i,j],img2[i,jj+1],img2[ii+1,j-1],img2[ii+1,j],img2[ii,jj+1]]
    for temp in colorij:
      tlist.append(sqrt((temp[0]-0)^2+(temp[1]-0)^2+(temp[2]-0)^2))
    select=min(tlist)
    r,g,b=0,0,0
    for temp in colorij:
      if sqrt((temp[0]-0)^2+(temp[1]-0)^2+(temp[2]-0)^2)==select:
        r=temp[0]
        g=temp[1]
        b=temp[2]
    img3[i,j]=(r,g,b)

cv2.imwrite('1.png',img3)
