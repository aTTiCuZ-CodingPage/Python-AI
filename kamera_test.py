import cv2

kamera = cv2.VideoCapture(0) #1

if not kamera.isOpened(): #2
    print('Kamera nicht geöffnet!')
else:
    input('Drücke ENTER, um ein Foto zu machen.') #3
    get, frame = kamera.read() #4
    graustufen = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #5
    print(graustufen) #6
    cv2.imshow('Geste', graustufen) #7
    cv2.waitKey(0) #8
kamera.release() #9