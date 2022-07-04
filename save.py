import cv2
from matplotlib import image
anh = cv2.imread("round.png",cv2.IMREAD_GRAYSCALE) # doc anh xam vao vien anh
cv2.imwrite("anhMauLuu.png",anh)
