
'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.4:
Práctica No.: 3
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:

-Crear un programa que lea una imagen y detecte bordes usando los operadores
de Roberts, Prewitt y Sobel. Visualizar en una ventana la imagen original y los resultados
obtenidos con los operadores (Roberts, Prewitt y Sobel) para detectar los bordes.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer imagen
img = cv2.imread('monedas.jpg')
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convertir a RGB para su posterior visualización

# Imagen de procesamiento en escala de grises
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Operador de Roberts
kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
kernely = np.array([[0, -1], [1, 0]], dtype=int)
x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)

# Operador Prewitt
kernelxPrewitt = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernelyPrewitt = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
x1 = cv2.filter2D(grayImage, cv2.CV_16S, kernelxPrewitt)
y1 = cv2.filter2D(grayImage, cv2.CV_16S, kernelyPrewitt)

# Operador Sobel
x2 = cv2.Sobel(grayImage, cv2.CV_16S, 1, 0)  # Encuentra la primera derivada de x
y2 = cv2.Sobel(grayImage, cv2.CV_16S, 0, 1)  # Encuentra la primera derivada de y
absX2 = cv2.convertScaleAbs(x2)
absY2 = cv2.convertScaleAbs(y2)
Sobel = cv2.addWeighted(absX2, 0.5, absY2, 0.5, 0)


absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


absX1 = cv2.convertScaleAbs(x1)
absY1 = cv2.convertScaleAbs(y1)
Prewitt = cv2.addWeighted(absX1, 0.5, absY1, 0.5, 0)

# Se usa para mostrar etiquetas chinas normalmente
plt.rcParams['font.sans-serif'] = ['SimHei']

# Mostrar gráficos
titles = [u'Imagen original ', u'Operador de Roberts', u'Operador de Prewitt',u'Operador de Sobel']
images = [img_RGB,Roberts,Prewitt,Sobel]
for i in range(4):
     plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
     plt.title(titles[i])
     plt.xticks([]), plt.yticks([])
plt.show()



