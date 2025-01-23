import numpy as np
from itertools import product
import copy
import math
import pickle

def sig(x):
    """Sigmoid Aktivierungsfunktion"""
    return 1 / (1 + math.e**-x)

def datenLesen(pfad, O_KNOTEN=10):
    """
    Liest und verarbeitet die MNIST Daten aus einer CSV-Datei
    
    Args:
        pfad: Pfad zur CSV-Datei
        O_KNOTEN: Anzahl der Ausgabeknoten (default: 10 für MNIST-Ziffern)
    
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

def parameter_search(base_model_state, parameter_ranges, I_KNOTEN=784, O_KNOTEN=10, PFAD_TRAINING='mnist_train.csv', PFAD_TEST='mnist_test.csv'):
    """
    Führt eine Rastersuche über verschiedene Hyperparameter durch
    
    Args:
        base_model_state: Dictionary mit Basis-Modellparametern
        parameter_ranges: Dictionary mit zu testenden Parameterbereichen
        I_KNOTEN: Anzahl der Eingabeknoten (default: 784 für MNIST)
        O_KNOTEN: Anzahl der Ausgabeknoten (default: 10 für MNIST-Ziffern)
        PFAD_TRAINING: Pfad zur Trainingsdatei
        PFAD_TEST: Pfad zur Testdatei
    
    Returns:
        best_params: Dictionary mit den besten gefundenen Parametern
        best_accuracy: Beste erreichte Genauigkeit
        results: Liste aller Ergebnisse
    """
    results = []
    best_accuracy = 0
    best_params = None
    
    # Erstelle alle möglichen Parameterkombinationen
    param_names = list(parameter_ranges.keys())
    param_values = list(parameter_ranges.values())
    combinations = list(product(*param_values))
    
    for combo in combinations:
        # Erstelle aktuelle Parameterkonfiguration
        current_params = copy.deepcopy(base_model_state)
        for param_name, param_value in zip(param_names, combo):
            current_params[param_name] = param_value
            
        # Initialisiere Modell mit aktuellen Parametern
        global EPOCHEN, LR, H_KNOTEN, wih, who
        EPOCHEN = current_params['epochs']
        LR = current_params['learning_rate']
        H_KNOTEN = current_params['hidden_nodes']
        
        # Initialisiere Gewichte neu
        wih = np.random.rand(H_KNOTEN, I_KNOTEN) - 0.5
        who = np.random.rand(O_KNOTEN, H_KNOTEN) - 0.5
        
        # Trainiere und evaluiere
        print(f"\nTeste Parameter: {current_params}")
        
        # Training
        daten = datenLesen(PFAD_TRAINING, O_KNOTEN)
        if not daten:  # Überprüfe ob Daten erfolgreich geladen wurden
            continue
            
        for ep in range(EPOCHEN):
            print(f"Epoche {ep+1}/{EPOCHEN}", end='\r')
            for i, t in daten:
                trainieren(i, t)
        
        # Evaluation
        testbericht = []
        testdaten = datenLesen(PFAD_TEST, O_KNOTEN)
        if not testdaten:  # Überprüfe ob Testdaten erfolgreich geladen wurden
            continue
            
        for i, t in testdaten:
            o = vorhersagen(i)
            ziffer = np.argmax(o)
            erwarteteZiffer = np.argmax(t)
            testbericht.append(ziffer == erwarteteZiffer)
        
        accuracy = sum(testbericht) / len(testbericht)
        print(f"Genauigkeit: {accuracy*100:.2f}%")
        
        results.append({
            'params': current_params,
            'accuracy': accuracy
        })
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_params = current_params
    
    return best_params, best_accuracy, results

# Beispielaufruf mit Standard-MNIST-Dimensionen
parameter_ranges = {
    'epochs': [5],
    'learning_rate': [0.1],
    'hidden_nodes': [600]
}

base_model_state = {
    'epochs': 2,
    'learning_rate': 0.1,
    'hidden_nodes': 500
}

# Die Hauptfunktion
if __name__ == "__main__":
    best_params, best_accuracy, all_results = parameter_search(base_model_state, parameter_ranges)
    print("\nBeste gefundene Parameter:")
    print(f"Genauigkeit: {best_accuracy*100:.2f}%")
    print("Parameter:", best_params)

    # Sortiere und zeige alle Ergebnisse
    sorted_results = sorted(all_results, key=lambda x: x['accuracy'], reverse=True)
    print("\nAlle Ergebnisse (sortiert nach Genauigkeit):")
    for result in sorted_results:
        print(f"Genauigkeit: {result['accuracy']*100:.2f}% - Parameter: {result['params']}")

    stream = open('gewichte.dat', 'wb') #1
    pickle.dump((wih, who), stream) #2
    stream.close()

    