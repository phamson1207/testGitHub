from traceback import print_tb
import cv2
import numpy as np
from matplotlib import image
image = cv2.imread("roand.png")
frameReSize = cv2.resize(image,dsize=(711,400) )
ret,thresh1 = cv2.threshold(frameReSize,127,255,cv2.THRESH_BINARY)
for i in range(711):
    valueBGR = thresh1[200][i]
    total_Color = int(valueBGR[0])+ int(valueBGR[1])+int(valueBGR[2])
    if  total_Color < 700:
        print(i)
    valueBGR = thresh1[100][i]
    total_Color = int(valueBGR[0])+ int(valueBGR[1])+int(valueBGR[2])
    if  total_Color < 700:
        print(i)
    thresh1[200][i] = [0,0,255]
    thresh1[100][i] = [0,0,255]
   
    
     
cv2.imshow("",thresh1)
cv2.waitKey()
cv2.destroyAllWindows()