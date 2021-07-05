
'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.:2
Práctica No.: 1
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:
Crear un programa permita realizar transformaciones básicas a una imagen, tales
como: trasladar, rotar, escalar y sumar dos imágenes. Muestre los resultados en una sola
ventana.

'''

import cv2
import numpy as np

image = cv2.imread('lenna.jpg')
ancho = image.shape[1]  # columnas
alto = image.shape[0]  # filas

# Traslación
M = np.float32([[1, 0, 100], [0, 1, 150]])
imageOut = cv2.warpAffine(image, M, (ancho, alto))

cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotación
M = cv2.getRotationMatrix2D((ancho // 2, alto // 2), 15, 1)
imageOut = cv2.warpAffine(image, M, (ancho, alto))

cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Escalando una imagen
imageOut = cv2.resize(image, (600, 300), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()

# sumar imagenes
img1 = cv2.imread('cadena.jpg')
img2 = cv2.imread('sacapuntas.jpg')
resA = cv2.add(img1, img2)
cv2.imshow('resA', resA)
cv2.waitKey(0)
cv2.destroyAllWindows()
