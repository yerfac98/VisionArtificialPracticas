
'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.4:
Práctica No.: 3
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:

-Crear un programa que lea una imagen y segmente la imagen utilizando un
método de segmentación (sea local o global). Visualizar en una ventana la imagen original
y el resultado de la segmentación del objeto u objetos.
'''

from pylab import *
import cv2

imagen = cv2.imread('monedas.jpg')
rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# _, ax1 = subplots(1, figsize=(16, 4))
# l, ax2 = subplots(1, figsize=(16, 4))
cv2.imshow('Original', imagen)


# ax2.imshow(gray)

def canny(image, sigma=0.33):
    v = np.median(image)

    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    return edged


edges = canny(gray)

# imshow(edges, cmap="gray")
# show()

# Buscar los contornos de las bolas y los dibujar en verde
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(rgb, contours, -1, (0, 255, 0), 2)
cv2.imshow('Segmentacion', rgb)
cv2.waitKey(0)
