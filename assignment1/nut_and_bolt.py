import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/guru/Desktop/assigment/assignment1/nuts_and_bolt/all/50x50/test/nuts/reszd_0052.jpg',0)
no_of_rows,_ = np.shape(img)
img = cv2.GaussianBlur(img,(5,5),0)
ret3,res = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
change=res[no_of_rows//2][0]
count=0
for value in res[no_of_rows//2]:
	if change!=value:
		count+=1
		change=value
if count>2:
	print("it's a nut")
else:
	print("it's a bolt")