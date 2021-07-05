

'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.:2
Práctica No.:1
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021
Descripción del problema de la práctica:
-Crear un programa que lea una imagen a color y convierta el escala de grises,
además muestre en una ventana. la imagen original y la imagen en escala de grises.


'''
import cv2

image = cv2.imread('lenna.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('OpenCV Python - Original', image)
cv2.imshow('OpenCV Python - Gray', gray)
cv2.waitKey(0)
