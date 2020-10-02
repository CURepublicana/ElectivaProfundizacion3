import matplotlib.pyplot as plt
import numpy as np
import cv2
imagen = np.zeros((500,500, 3), dtype=np.int16)
imagen.shape
#crear un  rectángulo
cv2.rectangle(imagen, pt1=(250, 300), pt2=(320, 400), color=(106,50,255), thickness=10)
cv2.rectangle(imagen, pt1=(150, 150), pt2=(200, 200), color=(116,60,30), thickness=10)
#crear un círculo
cv2.circle(imagen, center=(5, 40), radius=30, color=(220/2, 35*3, 24+5), thickness=5)
cv2.circle(imagen, center=(250, 250), radius=100, color=(220/2, 35*3, 24+5), thickness=5)
#crear línea
cv2.line(imagen, pt1=(0,400), pt2=(500,400), color=(225, 50, 75), thickness=10)
cv2.line(imagen, pt1=(25,125), pt2=(25,500), color=(225, 50, 75), thickness=10)
#elipsís
center_coordinates = (120, 100) 
axesLength = (100, 50)
startAngle = 0
endAngle = 360
# Blue color in BGR 
color = (255, 0, 0) 
cv2.ellipse(imagen,center_coordinates,axesLength,45,startAngle,endAngle,color,10)
plt.imshow(imagen)