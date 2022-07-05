import cv2
from numpy import imag
imgae = cv2.imread("anhMau.png")
imgaeHSV =imgae
frameReSize = cv2.resize(imgaeHSV,dsize=(400,400) ) # co dinh kich thuoc khung hinh
cv2.imshow("",imgae)
for i in range(400):
    for j in range (400):
        temp = frameReSize[i][j] 
        temp[0] = 0
        temp[2] = 0
        frameReSize[i][j] = temp

cv2.imshow("",frameReSize)
cv2.waitKey()
cv2.destroyAllWindows()