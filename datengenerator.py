# datengenerator.py
from random import shuffle
ZEILE = '{},{},{},{},{},{}\n' #1
d = [(1, 0, 0, 0, 1, 0), (0, 1, 0, 0, 1, 0),
    (0, 0, 1, 0, 1, 0), (0, 0, 0, 1, 1, 0),
    (1, 1, 0, 0, 0, 1), (0, 0, 1, 1, 0, 1),
    (1, 0, 1, 0, 0, 1), (0, 1, 0, 1, 0, 1),
    (1, 1, 0, 0, 0, 1), (0, 0, 1, 1, 0, 1),
    (1, 0, 0, 1, 0, 1), (0, 1, 1, 0, 0, 1)] #2
daten = 1000 * d #3
shuffle(daten)
trainingsdaten = '' #4
for i1, i2, i3, i4, t1, t2 in daten: #5
    trainingsdaten += ZEILE.format(i1, i2, i3, i4, t1, t2) #6
trainingsdaten += '1,0,0,0,1,0' #7
stream = open('apfel_gurke_trainingsdaten.csv', 'w') #8
stream.write(trainingsdaten)
stream.close()