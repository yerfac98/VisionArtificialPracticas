
'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.:2
Práctica No.: 1
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:
-Crear un programa que permita leer una imagen y lo muestre en una ventana.

'''
import cv2
import numpy as np

img = cv2.imread("lenna.jpg", 1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

