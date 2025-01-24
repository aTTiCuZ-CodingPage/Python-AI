# --------------------------------------------------------------
# gesichter.py
# Aus einem Farbbild werden alle Gesichter erfasst und gezählt.
# Alle Gesichter werden durch einen grauen Kasten unkenntlich gemacht.
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 8
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
import cv2
FOTO = 'bilder/Pic-0007.jpg'
XMLDATEI = 'haarcascade_frontalface_default.xml'
img = cv2.imread(FOTO)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
klassifizierer = cv2.CascadeClassifier(XMLDATEI)
rechtecke = klassifizierer.detectMultiScale(gray,
                                            scaleFactor=1.05,
                                            minNeighbors=5)
n = len(rechtecke)
print('Ich habe', n, 'Gesichter gefunden.')

for x,y,w,h  in rechtecke:
    cv2.rectangle(img, (x, y), (x+w, y+h), (150, 150, 150), -1)   
cv2.imshow('Foto mit unkenntlich gemachten Gesichtern', img)
cv2.waitKey(0)                 # warte bis Taste gedrückt
cv2.destroyAllWindows()        # Schließe das Viewer-Fenster
