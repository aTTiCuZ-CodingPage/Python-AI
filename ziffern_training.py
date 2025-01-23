import numpy as np
import math

# Hyperparameter
EPOCHEN = 5  # Anzahl Trainingsdurchläufe
LR = 0.1     # Lernrate

# Netzwerk-Architektur
I_KNOTEN = 784  # Eingabeknoten (28x28 Pixel)
H_KNOTEN = 700  # Hidden Layer Knoten
O_KNOTEN = 10   # Ausgabeknoten (Ziffern 0-9)

# Datenpfade
PFAD_TRAINING = 'mnist_train.csv'
PFAD_TEST = 'mnist_test.csv'

# Initialisierung der Gewichtsmatrizen
wih = np.random.rand(H_KNOTEN, I_KNOTEN) - 0.5
who = np.random.rand(O_KNOTEN, H_KNOTEN) - 0.5

def sig(x):
    """Sigmoid Aktivierungsfunktion"""
    return 1 / (1 + math.e**-x)

def datenLesen(pfad):
    """
    Liest und verarbeitet die MNIST Daten aus einer CSV-Datei
    Returns: Liste von Tupeln (Eingabe-Matrix, Target-Matrix)
    """
    try:
        with open(pfad, 'r') as stream:
            datenliste = stream.readlines()
        
        daten = []
        for zeile in datenliste:
            # Zerlege CSV-Zeile
            zeileListe = zeile.split(',')
            
            # Verarbeite Eingabewerte
            eingaben = np.array(zeileListe[1:], dtype=float)
            eingabenSkaliert = (eingaben/255 * 0.99) + 0.01  # Skalierung auf 0.01-1.0
            
            # Erstelle One-Hot-Encoded Target
            targets = np.zeros(O_KNOTEN) + 0.01
            targets[int(zeileListe[0])] = 0.99
            
            # Forme Arrays in Matrix um
            i = np.array(eingabenSkaliert, ndmin=2).T
            t = np.array(targets, ndmin=2).T
            
            daten.append((i, t))
            
        return daten
    except FileNotFoundError:
        print(f"Fehler: Die Datei {pfad} wurde nicht gefunden.")
        return []
    except Exception as e:
        print(f"Fehler beim Lesen der Datei: {e}")
        return []

def trainieren(i, t):
    """Trainiert das neuronale Netz mit einem Beispiel"""
    global wih, who
    
    # Forward Pass
    xh = np.dot(wih, i)
    yh = sig(xh)
    xo = np.dot(who, yh)
    o = sig(xo)
    
    # Backpropagation
    eo = t - o
    eh = np.dot(who.T, eo)
    who += LR * np.dot((eo * o * (1.0 - o)), yh.T)
    wih += LR * np.dot((eh * yh * (1.0 - yh)), i.T)

def vorhersagen(i):
    """Macht eine Vorhersage für eine Eingabe"""
    xh = np.dot(wih, i)
    yh = sig(xh)
    xo = np.dot(who, yh)
    return sig(xo)

def main():
    # Training
    print("Starte Training...")
    for ep in range(EPOCHEN):
        print(f"Epoche {ep+1}/{EPOCHEN}")
        daten = datenLesen(PFAD_TRAINING)
        if not daten:
            return
        for i, t in daten:
            trainieren(i, t)
    
    # Testing
    print("\nStarte Evaluation...")
    testbericht = []
    testdaten = datenLesen(PFAD_TEST)  # Korrigiert: PFAD_TEST statt PFAD_TRAINING
    if not testdaten:
        return
    
    for i, t in testdaten:
        o = vorhersagen(i)
        ziffer = np.argmax(o)
        erwarteteZiffer = np.argmax(t)
        testbericht.append(ziffer == erwarteteZiffer)
    
    trefferquote = sum(testbericht) / len(testbericht)
    print('Trefferquote: {:.2f}%'.format(trefferquote * 100))

if __name__ == "__main__":
    main()