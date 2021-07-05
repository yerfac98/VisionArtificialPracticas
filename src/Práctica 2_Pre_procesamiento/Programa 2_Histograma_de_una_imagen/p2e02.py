'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.:3
Práctica No.: 2
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:

-Crear un programa que lea una imagen y obtenga su histograma. Visualizar
la imagen original, en escala de grises y su histograma.
'''
import matplotlib.pyplot as plt
import cv2


def plot_demo(image):
    print(image.ravel())  ##ravel Convierte imágenes 3D en matrices 1D para frecuencia estadística
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()


src = cv2.imread('lenna.jpg')
cv2.imshow('Entrada de imagen', src)
# imprimir en escala de grises
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow('Escala de grises', gray)

plot_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
