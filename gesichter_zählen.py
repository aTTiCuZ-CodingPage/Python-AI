import cv2

FOTO = 'bilder/Pic-0007.jpg'
XMLDATEI = 'haarcascade_frontalface_default.xml'

bild = cv2.imread(FOTO) #1
grau = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY) #2
klassifizierer = cv2.CascadeClassifier(XMLDATEI) #3
rechtecke = klassifizierer.detectMultiScale(grau, 
                                            scaleFactor=1.05, 
                                            minNeighbors=5) #4

n = len(rechtecke) #5

print('Ich habe', n, 'Gesichter gefunden.') #6
x, y, w, h = rechtecke[0] #7

cv2.rectangle(bild, (x, y), (x+w, y+h), (0, 255, 255), 2) #8
cv2.imshow('Foto mit dem ersten erkannten Gesicht', bild) #9
cv2.waitKey(0) #10
cv2.destroyAllWindows() #11