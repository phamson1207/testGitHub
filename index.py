from tkinter import Frame
import cv2
import imutils
idCamera = 0 # gia tri dc gan mac dinh cho camera thu nhat
cap = cv2.VideoCapture(idCamera) # mo video
anh1 = cv2.imread("round.png",cv2.COLOR_BGR2HSV)  # doc file anh
#anh1 = cv2.imread("anhMau.png",cv2.IMREAD_GRAYSCALE)  # doc file anh den trang
#anh2 = cv2.imread("anhMau.png",cv2.IMREAD_ANYCOLOR) doc cac dinh dang anh khac ngoai BGR 
cv2.imshow("anh1",anh1)
while True:
    ret,frame = cap.read() # fram nhan ve du lieu tu khung hinh, ret kiem tra qtinh dung sai cuar khung hinh
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frameReSize = cv2.resize(frame,dsize=(400,400) ) # co dinh kich thuoc khung hinh
    frame = imutils.rotate(frame,90)
  
    cv2.imshow("cam",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):# doi an nut q la thoat
        break
#cv2.imshow("anh1",anh1)
#cv2.imshow("anh2",anh2)
cap.release() #giai phong camera
cv2.destroyAllWindows() # dong tat ca cac cua so dang mo

