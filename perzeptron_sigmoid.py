# perzeptron_sigmoid.py
from math import e #1
DATEN = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
LR = 0.1
B = - 0.5 #2
w1 = 0.5
w2 = 0.5



def sig(x): #3
    return 1 / (1 + e**-x)

def trainieren(i1, i2, t):
    global w1, w2
    o = vorhersehen(i1, i2)
    w1 += LR * (t - o) * i1
    w2 += LR * (t - o) * i2

def vorhersehen(i1, i2):
    x = w1 * i1 + w2 * i2 + B #4
    return sig(x) #5

for epoche in range(10):
    for i1, i2, t in DATEN:
        trainieren(i1, i2, t)

for i1, i2, t in DATEN:
    o = vorhersehen(i1, i2)
    print('Eingaben:',i1, i2,
        'Ausgabe:', o, 'Erwartet:', t)