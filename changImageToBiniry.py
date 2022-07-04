# duong anh ve muc 0->255
from tkinter import Frame
import cv2
import imutils

anh2 = cv2.imread("round.png",0)  # doc file anh
cv2.imshow("anh123",gray_image)
cv2.waitKey()
gray_image = cv2.cvtColor(anh2,cv2.COLOR_BGR2GRAY)

