import numpy as np
import cv2
import matplotlib.pyplot as plt

#definimos la función para dibujar
def dibujar(event, x,y, etiquetas, parametros):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x,y), 20, (255,0,0), -1)

#CONECTAR LA IMAGEN CON LA FUNCION
cv2.namedWindow(winname='Mi_Imagen')
cv2.setMouseCallback('Mi_Imagen', dibujar)

#detectar imagen y dibujar
imagen = np.zeros((500, 500, 3), np.int8)

while True:
    
    cv2.imshow('Mi_Imagen', imagen)
    
    if cv2.waitKey(10) & 0xFF == 27:
        break
    
cv2.destroyAllWindow()
