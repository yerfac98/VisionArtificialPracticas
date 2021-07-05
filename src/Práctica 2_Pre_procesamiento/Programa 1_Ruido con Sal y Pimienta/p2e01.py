
'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.:3
Práctica No.: 2
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:

-Crear un programa que permita generar ruido usando la técnica salt&paper
(sal y pimienta) a una imagen de entrada y guardar la imagen con ruido en el formato
de imagen que desee (por ejemplo en PNG o JPG). Visualizar la imagen original y la
imagen con ruido en una ventana.
'''

import numpy as np
import cv2
import random

# Función para añadir ruido sal y pimienta a una imagen
def sp_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


frame = cv2.imread('lenna.jpg')

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', gray)

k = cv2.waitKey(0)

noise_img = sp_noise(gray, 0.05)

cv2.imshow('ruidosa', noise_img)

k = cv2.waitKey(0)
cv2.imwrite('lennaRuido.jpg',noise_img)
cv2.destroyAllWindows()
