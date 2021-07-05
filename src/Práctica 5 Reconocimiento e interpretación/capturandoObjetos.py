'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.6:
Práctica No.: 5
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:

-Crear una aplicación que permita reconocer algún tipo de objeto de su preferencia
utlizando la librería OpenCV y el calisifcador Haarcascade. Por ejemplo, puede considerar
reconocer sea botellas, lapiceros, celulares, gatos, perros u otro objeto de su preferencia.
Como entrada a la aplicación deberá recibir una secuencia de imágenes o vídeo usando
la webcam y determinar el tipo de objeto que encuentra en la imagen o vídeo usando la
webcam.
'''

import cv2
import numpy as np
import imutils
import os

Datos = 'p'
if not os.path.exists(Datos):
    print('Carpeta creada: ',Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0
while True:

    ret, frame = cap.read()
    if ret == False: break
    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

    objeto = imAux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto,width=38)
    #print(objeto.shape)

    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
        print('Imagen guardada:'+'/objeto_{}.jpg'.format(count))
        count = count +1
    if k == 27:
        break

    cv2.imshow('frame',frame)
    cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()