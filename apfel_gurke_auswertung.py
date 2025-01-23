# nn_4_3_2.py
from random import uniform, shuffle
from math import e

W = 1
LR = 0.1

wi1h1 = uniform(-W, W) #1
wi2h1 = uniform(-W, W)
wi3h1 = uniform(-W, W)
wi4h1 = uniform(-W, W)
wi1h2 = uniform(-W, W)
wi2h2 = uniform(-W, W)
wi3h2 = uniform(-W, W)
wi4h2 = uniform(-W, W)
wi1h3 = uniform(-W, W)
wi2h3 = uniform(-W, W)
wi3h3 = uniform(-W, W)
wi4h3 = uniform(-W, W)
wh1o1 = uniform(-W, W)
wh2o1 = uniform(-W, W)
wh3o1 = uniform(-W, W)
wh1o2 = uniform(-W, W)
wh2o2 = uniform(-W, W)
wh3o2 = uniform(-W, W)
def sig(x):
    return 1.0 / (1.0 + e**-x)

def vorhersagen(i1, i2, i3, i4): #2
    xh1 = wi1h1 * i1 + wi2h1 * i2 + wi3h1 * i3 + wi4h1 * i4
    xh2 = wi1h2 * i1 + wi2h2 * i2 + wi3h2 * i3 + wi4h2 * i4
    xh3 = wi1h3 * i1 + wi2h3 * i2 + wi3h3 * i3 + wi4h3 * i4
    yh1 = sig(xh1)
    yh2 = sig(xh2)
    yh3 = sig(xh3)
    xo1 = yh1 * wh1o1 + yh2 * wh2o1 + yh3 * wh3o1
    xo2 = yh1 * wh1o2 + yh2 * wh2o2 + yh3 * wh3o2
    o1 = sig(xo1)
    o2 = sig(xo2)
    return o1, o2

def trainieren(i1, i2, i3, i4, t1, t2): #3
    global wi1h1, wi2h1, wi1h2, wi2h2, wi1h3, wi2h3
    global wi3h1, wi4h1, wi3h2, wi4h2, wi3h3, wi4h3 #4
    global wh1o1, wh2o1, wh3o1, wh1o2, wh2o2, wh3o2
    # Berechnung der Ausgabe (Vorhersage)
    xh1 = wi1h1 * i1 + wi2h1 * i2 + wi3h1 * i3 + wi4h1 * i4 #5
    xh2 = wi1h2 * i1 + wi2h2 * i2 + wi3h2 * i3 + wi4h2 * i4
    xh3 = wi1h3 * i1 + wi2h3 * i2 + wi3h3 * i3 + wi4h3 * i4
    yh1 = sig(xh1)
    yh2 = sig(xh2)
    yh3 = sig(xh3)
    xo1 = yh1 * wh1o1 + yh2 * wh2o1 + yh3 * wh3o1
    xo2 = yh1 * wh1o2 + yh2 * wh2o2 + yh3 * wh3o2
    o1 = sig(xo1)
    o2 = sig(xo2)
    # Aktualisierung der Gewichte
    eo1 = t1 - o1
    eo2 = t2 - o2
    wh1o1 += LR * eo1 * o1*(1-o1)*yh1
    wh2o1 += LR * eo1 * o1*(1-o1)*yh2
    wh3o1 += LR * eo1 * o1*(1-o1)*yh3
    wh1o2 += LR * eo2 * o2*(1-o2)*yh1
    wh2o2 += LR * eo2 * o2*(1-o2)*yh2
    wh3o2 += LR * eo2 * o2*(1-o2)*yh3
    eh1 = wh1o1 * eo1 + wh1o2 * eo2
    eh2 = wh2o1 * eo1 + wh2o2 * eo2
    eh3 = wh3o1 * eo1 + wh3o2 * eo2
    wi1h1 += LR * eh1 * yh1*(1-yh1)*i1
    wi2h1 += LR * eh1 * yh1*(1-yh1)*i2
    wi3h1 += LR * eh1 * yh1*(1-yh1)*i3 #6
    wi4h1 += LR * eh1 * yh1*(1-yh1)*i4
    wi1h2 += LR * eh2 * yh2*(1-yh2)*i1
    wi2h2 += LR * eh2 * yh2*(1-yh2)*i2
    wi3h2 += LR * eh2 * yh2*(1-yh2)*i3
    wi4h2 += LR * eh2 * yh2*(1-yh2)*i4
    wi1h3 += LR * eh3 * yh3*(1-yh3)*i1
    wi2h3 += LR * eh3 * yh3*(1-yh3)*i2
    wi3h3 += LR * eh3 * yh3*(1-yh3)*i3
    wi4h3 += LR * eh3 * yh3*(1-yh3)*i4
    return eo1, eo2

def datenLesen(dateiname):
    f = open(dateiname, 'r') #7
    datenliste = f.readlines() #8
    f.close()
    daten = [] #9
    for zeile in datenliste: #10
        i1, i2, i3, i4, t1, t2 = zeile.split(',') #11
        daten.append((int(i1), int(i2),
                      int(i3), int(i4),
                      int(t1), int(t2))) #12
    return daten #13

daten = datenLesen('apfel_gurke_trainingsdaten.csv') #14
for ep in range(10): #15
    summeFehlerQuadrate = 0
    for i1, i2, i3, i4, t1, t2 in daten: #16
        eo1, eo2 = trainieren(i1, i2, i3, i4, t1, t2) #17
        summeFehlerQuadrate += eo1**2 + eo2**2 #18
    mFehlerQuadrate = summeFehlerQuadrate / len(daten) #19
print('Fehlerquadratsumme (letzte Epoche):', mFehlerQuadrate) #20

eingabe = 'j' #21
while eingabe == 'j': #22
    i1 = int(input('1. Pixel (1 = schwarz, 0 = weiß): ')) #23
    i2 = int(input('2. Pixel (1 = schwarz, 0 = weiß): '))
    i3 = int(input('3. Pixel (1 = schwarz, 0 = weiß): '))
    i4 = int(input('4. Pixel (1 = schwarz, 0 = weiß): '))
    o1, o2 = vorhersagen(i1, i2, i3, i4) #24
    if o1 > 0.5 and o2 < 0.5: #25
        print('Apfel') #26
    elif o1 < 0.5 and o2 > 0.5: #27
        print('Gurke')
    else:
        print('Objekt nicht erkannt') #28
    eingabe = input('Noch einmal? (j/n): ') #29
    print('Auf Wiedersehen!')