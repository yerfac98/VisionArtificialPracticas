
'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.:2
Práctica No.: 1
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:
Crear un programa que capture vídeo streaming (usando la webcam) y guarde
en un archivo de vídeo en formato MP4 o AVI. Mostrar en una ventana el vídeo streaming
(leido desde la webcam) y su correspondiente en escala de grises.


'''
import cv2

captura = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('salida.mp4', fourcc, 20.0, (640, 480))
while True:
    ret, frame = captura.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    out.write(frame)
    try:
        cv2.imshow('frame2', gray)
        out.write(gray)
    except:
        print('ERROR')
    if cv2.waitKey(0)& 0xFF == ord('q'):
        break


captura.release()
out.release()
cv2.destroyAllWindows()
del (captura)

