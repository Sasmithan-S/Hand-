import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    #lecture
    ret, frame = cap.read()
    #affichage de l'image 
    #cv2.imshow("Vue ", frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    bleu_haut = np.array([130, 255, 255])
    bleu_bas = np.array([90, 50, 50])
    masque = cv2.inRange(hsv, bleu_bas, bleu_haut)


    cv2.imshow("detection_bleu",masque)
    contours, _ = cv2.findContours(masque, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours: 
         plus_gros_contour = max(contours, key=cv2.contourArea)
         M = cv2.moments(plus_gros_contour)
         #calcul du centre de la cours la plus présente (moyenne x y)
         if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            #  point rouge au centre 
            cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)
            print(f"Cible bleue trouvée en X:{cx} Y:{cy}")


    cv2.imshow("Vue ", frame)
    #masque pour prendre que les 8 premiers bits en compte     
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break



cap.release()
cv2.destroyAllWindows()