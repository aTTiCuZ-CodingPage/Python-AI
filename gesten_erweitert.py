#----------------------------------------------------------------
# Dateiname: gesten_erweitert.py
#
# Das Programm macht mit der angeschlossenen Kamera (Kanal 0)
# Bilder, trainiert zwei Gesten ein und kann
# nach dem Training die zwei Gesten unterscheiden. 
# Erweiterte Version (Lösung Aufgabe 4).
#
# Künstliche Intelligenz kapieren und programmieren
# Kapitel 7
# Michael Weigend 19.9.2023
# --------------------------------------------------------------
import cv2
import numpy as np
import math

EPOCHEN = 100     # Anzahl Trainingsdurchläufe
LR = 0.1          # Lernrate
             
H_KNOTEN = 100    # Anzahl verborgene Knoten
O_KNOTEN = 2      # Anzahl Ausgabeknoten               


kamera = cv2.VideoCapture(0)                           

def sig(x):
    return 1 / (1 + math.e **-x)

def bildLesen():                                       
    get, bild = kamera.read()
    cv2.imshow('Kontrollbild', bild)                  #1
    cv2.waitKey(0)                                    #2
    grau = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)                  
    kleinesBild = cv2.resize(grau, (breite, höhe))                           
    eingaben = kleinesBild.reshape(1, I_KNOTEN)       
    return (eingaben/255).T                           
       
def trainieren(i, t):
    global wih, who      
    xh = np.dot(wih, i)
    yh = sig(xh)      
    xo = np.dot(who, yh)
    o = sig(xo)     
    eo = t - o  
    eh = np.dot(who.T, eo)   
    who += LR * np.dot((eo * o * (1.0 - o)), yh.T)  
    wih += LR * np.dot((eh * yh * (1.0 - yh)), i.T)

def vorhersagen(i):
    xh = np.dot(wih, i)
    yh = sig(xh)        
    xo = np.dot(who, yh)
    o = sig(xo)
    return o

# Trainingsdaten erfassen
ersteGeste = input('Name der ersten Geste: ')
zweiteGeste = input('Name der zweiten Geste: ')
anzahl = int(input('Wie viele Bilder von jeder Geste? '))
breite = int(input('Bildbreite in Pixel (z.B. 30): '))     #3
höhe = int(input('Bildhöhe in Pixel (z.B. 24): '))
I_KNOTEN = breite * höhe                                   #4
wih = np.random.rand(H_KNOTEN, I_KNOTEN) - 0.5             #5
who = np.random.rand(O_KNOTEN, H_KNOTEN) - 0.5
daten = []

for n in range(anzahl):
    input('Mache "' + ersteGeste + '" und drücke ENTER.')
    i = bildLesen()
    t = np.array([1, 0], ndmin=2).T
    daten.append((i, t))
    input('Mache "' + zweiteGeste + '" und drücke ENTER.')
    i = bildLesen()    
    t = np.array([0, 1], ndmin=2).T
    daten.append((i, t))

# Neuronales Netz trainieren
print('Ich trainiere ...')
for ep in range(EPOCHEN):
    for i, t in daten:
        trainieren(i, t)
    
# Neuronales Netz testen
eingabe = 'j'
while eingabe == 'j':
    input('Mache eine Geste und drücke ENTER!')
    i = bildLesen()
    o = vorhersagen(i)
    print('Ausgabe des neuronalen Netzes:',
          o[0,0], o[1,0])                                  #6
    if np.argmax(o) == 0:
        print('Ich erkenne: "' + ersteGeste + '".')
    else:
        print('Ich erkenne: "' + zweiteGeste + '".')
    eingabe = input('Noch einmal? (j/n) ')

