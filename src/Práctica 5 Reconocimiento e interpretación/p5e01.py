'''
Nombre de la institución: ITSTA
Carrera: Ingeniería en Sistemas Computacionales
Asignatura: Desarrollo de Aplicaciones con Visión Artificial
Unidad No.6:
Práctica No.: 5
Nombre del estudiante: Gerardo Facundo Del Angel
Fecha de entrega: 04/07/2021

Descripción del problema de la práctica:

-Crear una aplicación que permita reconocer algún tipo de objeto de su preferencia
utlizando la librería OpenCV y el calisifcador Haarcascade. Por ejemplo, puede considera
reconocer sea botellas, lapiceros, celulares, gatos, perros u otro objeto de su preferencia.
Como entrada a la aplicación deberá recibir una secuencia de imágenes o vídeo usando
la webcam y determinar el tipo de objeto que encuentra en la imagen o vídeo usando la
webcam.
'''
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

vasoClassif = cv2.CascadeClassifier('cascade.xml')

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    toy = vasoClassif.detectMultiScale(gray, scaleFactor=5,
                                       minNeighbors=91,
                                       minSize=(70, 78))

    for (x, y, w, h) in toy:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Vaso detectado', (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
