import numpy as np
from math import e
from random import shuffle

LR = 0.2

def sig(x):
    return 1.0 / (1.0 + e**-x)

# Initialisierung der Gewichte mit korrekten Dimensionen
wih = np.random.rand(3, 2) - 0.5  # 3x2 Matrix für Input->Hidden
who = np.random.rand(2, 3) - 0.5  # 2x3 Matrix für Hidden->Output

def vorhersagen(i):
    # i hat Dimension (2,1)
    xh = np.dot(wih, i)        # (3,2) x (2,1) = (3,1)
    yh = sig(xh)               # (3,1)
    xo = np.dot(who, yh)       # (2,3) x (3,1) = (2,1)
    o = sig(xo)                # (2,1)
    return o

def trainieren(i, t):
    global wih, who
    
    # Forward Pass
    xh = np.dot(wih, i)        # (3,2) x (2,1) = (3,1)
    yh = sig(xh)               # (3,1)
    xo = np.dot(who, yh)       # (2,3) x (3,1) = (2,1)
    o = sig(xo)                # (2,1)
    
    # Backpropagation
    eo = t - o                 # (2,1)
    delta_o = eo * o * (1.0 - o)  # (2,1)
    who += LR * np.dot(delta_o, yh.T)  # (2,1) x (1,3) = (2,3)
    
    eh = np.dot(who.T, delta_o)  # (3,2) x (2,1) = (3,1)
    delta_h = eh * yh * (1.0 - yh)  # (3,1)
    wih += LR * np.dot(delta_h, i.T)  # (3,1) x (1,2) = (3,2)
    
    return eo

# Trainingsdaten
d = [(0, 0, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 1)]
daten = 2000 * d
shuffle(daten)

# Training
for ep in range(10):
    summeFehlerQuadrate = 0
    for i1, i2, t1, t2 in daten:
        i = np.array([[i1], [i2]])      # (2,1) Matrix
        t = np.array([[t1], [t2]])      # (2,1) Matrix
        eo = trainieren(i, t)
        summeFehlerQuadrate += np.sum(eo**2)
    mFehlerQuadrate = summeFehlerQuadrate / len(daten)
    print('Epoche:', ep, 'mittlere Fehlerquadratsumme:', mFehlerQuadrate)

# Test
print("\nTestvorhersagen:")
for i1, i2, t1, t2 in d:
    i = np.array([[i1], [i2]])
    vorhersage = vorhersagen(i)
    print(f"Eingabe: ({i1}, {i2}) -> Vorhersage: ({vorhersage[0,0]:.3f}, {vorhersage[1,0]:.3f})")