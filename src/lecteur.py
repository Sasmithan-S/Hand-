import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    #lecture
    ret, frame = cap.read()
    #affichage de l'image 
    #cv2.imshow("Vue ", frame)

    gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("vue",gris)

    #masque pour prendre que les 8 premiers bits en compte     
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break



cap.release()
cv2.destroyAllWindows()