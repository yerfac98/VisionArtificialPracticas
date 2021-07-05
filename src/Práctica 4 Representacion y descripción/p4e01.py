'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.5:
Práctica No.: 4
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:

-A partir de una lectura de imagen de figuras geométricas, el programa detecta el tipo de figura geométrica
que es (triangulo, cuadrado, rectángulo, pentágono, hexágono, circulo) remarcando su contorno.
'''
import cv2

image = cv2.imread('figurasColores.png')
# transformarla a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# obtener una imagen binarizada mediante canny(deteccion de bordes)
canny = cv2.Canny(gray, 10, 150)
# Aplicamos dilatación y erosión para mejorar la imagen binaria obtenida
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

# encontrar todos los contornos correspondientes a la imagen binaria
cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # OpenCV 4
# se dibuja todos los contornos
cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)
# analizar cada uno de los contornos encontrados

for c in cnts:
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    # print(len(approx))
    x, y, w, h = cv2.boundingRect(approx)
    # Determinando las figuras geométricas
    if len(approx) == 3:
        cv2.putText(image, 'Triangulo', (x, y - 5), 1, 1, (0, 255, 0), 1)

    if len(approx) == 4:
        aspect_ratio = float(w) / h
        print('aspect_ratio= ', aspect_ratio)
        if aspect_ratio == 1:
            cv2.putText(image, 'Cuadrado', (x, y - 5), 1, 1, (0, 255, 0), 1)
        else:
            cv2.putText(image, 'Rectangulo', (x, y - 5), 1, 1, (0, 255, 0), 1)

    if len(approx) == 5:
        cv2.putText(image, 'Pentagono', (x, y - 5), 1, 1, (0, 255, 0), 1)

    if len(approx) == 6:
        cv2.putText(image, 'Hexagono', (x, y - 5), 1, 1, (0, 255, 0), 1)

    if len(approx) > 10:
        cv2.putText(image, 'Circulo', (x, y - 5), 1, 1, (0, 255, 0), 1)

    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    cv2.imshow('image', image)
    cv2.waitKey(0)
