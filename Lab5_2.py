import cv2, copy
import numpy as np
import os
from math import sqrt


def converse(img2, method):
    img3 = copy.deepcopy(img2)
    for i in range(0, img2.shape[0]):
        for j in range(0, img2.shape[1]):
            jj = j
            ii = i
            if jj == img2.shape[1] - 1: jj = -1
            if ii == img2.shape[0] - 1: ii = -1
            colorij = [img2[i - 1, j - 1], img2[i - 1, j], img2[i - 1, jj + 1], img2[i, j - 1], img2[i, j],
                       img2[i, jj + 1], img2[ii + 1, j - 1], img2[ii + 1, j], img2[ii + 1, jj + 1]]
            if method == 1 or method == 2:
                rx = colorij[2][0] + 2 * colorij[5][0] + colorij[8][0] - colorij[0][0] - 2 * colorij[3][0] - colorij[6][0]
                ry = colorij[0][0] + 2 * colorij[1][0] + colorij[2][0] - colorij[6][0] - 2 * colorij[7][0] - colorij[8][0]
                if method == 1: r = sqrt(rx ** 2 + ry ** 2)
                if method == 2: r = abs(rx) + abs(ry)
                gx = colorij[2][1] + 2 * colorij[5][1] + colorij[8][1] - colorij[0][1] - 2 * colorij[3][1] - colorij[6][1]
                gy = colorij[0][1] + 2 * colorij[1][1] + colorij[2][1] - colorij[6][1] - 2 * colorij[7][1] - colorij[8][2]
                if method == 1: g = sqrt(gx ** 2 + gy ** 2)
                if method == 2: g = abs(gx) + abs(gy)
                bx = colorij[2][2] + 2 * colorij[5][2] + colorij[8][2] - colorij[0][2] - 2 * colorij[3][2] - colorij[6][2]
                by = colorij[0][2] + 2 * colorij[1][2] + colorij[2][2] - colorij[6][2] - 2 * colorij[7][2] - colorij[8][2]
                if method == 1: b = sqrt(bx ** 2 + by ** 2)
                if method == 2: b = abs(bx) + abs(by)
            if method == 3 or method == 4:
                rx = int(colorij[8][0] - colorij[4][0])
                ry = int(colorij[7][0] - colorij[5][0])
                if method == 3: r = sqrt(rx ** 2 + ry ** 2)
                if method == 4: r = abs(rx) + abs(ry)
                gx = int(colorij[8][1] - colorij[4][1])
                gy = int(colorij[7][1] - colorij[5][1])
                if method == 3: g = sqrt(gx ** 2 + gy ** 2)
                if method == 4: g = abs(gx) + abs(gy)
                bx = int(colorij[8][2] - colorij[4][2])
                by = int(colorij[7][2] - colorij[5][2])
                if method == 3: b = sqrt(bx ** 2 + by ** 2)
                if method == 4: b = abs(bx) + abs(by)
                r = r + colorij[4][0]
                g = g + colorij[4][1]
                b = b + colorij[4][2]

            while (r < 0 or r > 255):
                if r < 0:
                    r = 0
                if r > 255:
                    r = 255
            while (g < 0 or g > 255):
                if g < 0:
                    g = 0
                if g > 255:
                    g = 255
            while (b < 0 or b > 255):
                if b < 0:
                    b = 0
                if b > 255:
                    b = 255
            img3[i, j] = (r, g, b)
    return img3



img = cv2.imread('123.png')
img[img == 255] = 254
print("\nSobel \n1 - sqrt(x*x+y*y) \n2 - abs(x)+abs(y) \nRoberts \n3 - sqrt(u*u+v*v) \n4 - abs(u)+abs(v)")
method = int(input("method: "))
img = converse(img, method)
cv2.imwrite('2.png', img)