'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.:3
Práctica No.: 2
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:
-Crear un programa que lea una imagen con ruido (use el programap2e01.py
para generar la imagen con ruido) y aplique elﬁltro promedio,ﬁltro gaussiano y el
ﬁltro mediana con kernels o máscaras de su preferencia (por ejemplo de3x3o de5x5).
Visualizar en una ventana la imagen original con ruido y los tresﬁltros aplicados
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lennaRuido.jpg")
cv2.imshow('original', img)

kernel = np.ones((3, 3), np.float32) / 9
f1 = cv2.filter2D(img, -1, kernel)
f2 = cv2.blur(img, (3, 3))
f3 = cv2.GaussianBlur(img, (3, 3), 0)
f4 = cv2.medianBlur(img, 3)

f = [f1, f2, f3, f4]
t = ['Convolucion', 'Promedio', 'Gaussiano', 'Mediana']
'''
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(f[i], vmin=0, vmax=255)
    plt.title(t[i])
    plt.xticks([]), plt.yticks([])
    plt.show()
'''
cv2.imshow('Convolucion', f1)
cv2.imshow('Promedio', f2)
cv2.imshow('Gausiano', f1)
cv2.imshow('Mediana', f1)


cv2.waitKey(0)
cv2.destroyAllWindows()


