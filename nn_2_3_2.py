# nn_2_3_2.py
from random import uniform, shuffle
from math import e
W = 0.5 #1
LR = 0.2 #2
wi1h1 = uniform(-W, W) #3
wi2h1 = uniform(-W, W)
wi1h2 = uniform(-W, W)
wi2h2 = uniform(-W, W)
wi1h3 = uniform(-W, W)
wi2h3 = uniform(-W, W)
wh1o1 = uniform(-W, W)
wh2o1 = uniform(-W, W)
wh3o1 = uniform(-W, W)
wh1o2 = uniform(-W, W)
wh2o2 = uniform(-W, W)
wh3o2 = uniform(-W, W)
def sig(x): #4
    return 1.0 / (1.0 + e**-x)

def vorhersagen(i1, i2): #5
    xh1 = wi1h1 * i1 + wi2h1 * i2 #6
    xh2 = wi1h2 * i1 + wi2h2 * i2
    xh3 = wi1h3 * i1 + wi2h3 * i2
    yh1 = sig(xh1) #7
    yh2 = sig(xh2)
    yh3 = sig(xh3)
    xo1 = yh1 * wh1o1 + yh2 * wh2o1 + yh3 * wh3o1 #8
    xo2 = yh1 * wh1o2 + yh2 * wh2o2 + yh3 * wh3o2
    o1 = sig(xo1) #9
    o2 = sig(xo2)
    return (o1, o2) #10

def trainieren(i1, i2, t1, t2): #11
    global wi1h1, wi2h1, wi1h2, wi2h2, wi1h3, wi2h3 #12
    global wh1o1, wh2o1, wh3o1, wh1o2, wh2o2, wh3o2
    # Berechnung der Ausgabe
    xh1 = wi1h1 * i1 + wi2h1 * i2 #13
    xh2 = wi1h2 * i1 + wi2h2 * i2
    xh3 = wi1h3 * i1 + wi2h3 * i2
    yh1 = sig(xh1)
    yh2 = sig(xh2)
    yh3 = sig(xh3)
    xo1 = yh1 * wh1o1 + yh2 * wh2o1 + yh3 * wh3o1
    xo2 = yh1 * wh1o2 + yh2 * wh2o2 + yh3 * wh3o2
    o1 = sig(xo1)
    o2 = sig(xo2)
    # Aktualisierung der Gewichte
    eo1 = t1 - o1 #14
    eo2 = t2 - o2
    wh1o1 += LR * eo1 * o1*(1-o1)* yh1 #15
    wh2o1 += LR * eo1 * o1*(1-o1)* yh2
    wh3o1 += LR * eo1 * o1*(1-o1)* yh3
    wh1o2 += LR * eo2 * o2*(1-o2)* yh1
    wh2o2 += LR * eo2 * o2*(1-o2)* yh2
    wh3o2 += LR * eo2 * o2*(1-o2)* yh3
    eh1 = wh1o1 * eo1 + wh1o2 * eo2 #16
    eh2 = wh2o1 * eo1 + wh2o2 * eo2
    eh3 = wh3o1 * eo1 + wh3o2 * eo2
    wi1h1 += LR * eh1 * yh1*(1-yh1)*i1 #17
    wi2h1 += LR * eh1 * yh1*(1-yh1)*i2
    wi1h2 += LR * eh2 * yh2*(1-yh2)*i1
    wi2h2 += LR * eh2 * yh2*(1-yh2)*i2
    wi1h3 += LR * eh3 * yh3*(1-yh3)*i1
    wi2h3 += LR * eh3 * yh3*(1-yh3)*i2
    return eo1, eo2 #18

d = [(0, 0, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 1)] #19
daten = 2000 * d #20
shuffle(daten) #21

for ep in range(10): #21
    summeFehlerQuadrate = 0 #22
    for i1, i2, t1, t2 in daten: #23
        eo1, eo2 = trainieren(i1, i2, t1, t2) #24
        summeFehlerQuadrate += eo1**2 + eo2**2 #25
    mFehlerQuadrate = summeFehlerQuadrate / len(daten) #26
    print('Epoche:',ep, 'mittlere Fehlerquadratsumme:',
    mFehlerQuadrate) #27

for i1, i2, t1, t2 in d: #28
    o1, o2 = vorhersagen(i1, i2) #29
    print('Eingabe:', i1, i2, 'Vorhersage: ',
        round(o1, 4), round(o2, 4),
        'Target:', t1, t2) #30