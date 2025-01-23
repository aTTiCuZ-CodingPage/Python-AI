# perzeptron.py
DATEN = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)] #1
LR = 0.1 #2
SW = 0.5 #3
w1 = 0.5 #4
w2 = 0.5

def vorhersehen(x1, x2): #5
    x = w1 * x1 + w2 * x2 #6
    if x > SW: #7
        return 1
    else:
        return 0
    
def trainieren(x1, x2, t): #8
    global w1, w2 #9
    o = vorhersehen(x1, x2) #10
    w1 += LR * (t - o) * x1 #11
    w2 += LR * (t - o) * x2

# Trainieren
for epoche in range(10): #12
    for x1, x2, t in DATEN: #13
        trainieren(x1, x2, t) #14
# Testen
for x1, x2, t in DATEN: #15
    o = vorhersehen(x1, x2) #16
    print('Eingaben:',x1, x2, 'Ausgabe:', o, 'Erwartet:', t) #17