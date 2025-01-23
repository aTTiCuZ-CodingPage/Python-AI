import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# b) Daten einlesen
def lade_daten(dateipfad):
    return pd.read_csv(dateipfad)

daten = lade_daten('pflanzen_daten.csv')

# c) Lineare Trennlinie berechnen
def berechne_trennlinie(daten):
    # Kodieren der Pflanzenarten in numerische Werte
    daten['Label'] = daten['Pflanzenart'].apply(lambda x: 1 if x == 'Weizen' else -1)
    
    # Feature-Matrix und Zielvariable
    X = daten[['x-Koordinate', 'y-Koordinate']].values
    y = daten['Label'].values
    
    # Hinzufügen einer Spalte für den Bias-Term (x0 = 1)
    X = np.hstack((np.ones((X.shape[0], 1)), X))
    
    # Berechnung der Gewichte mittels der Methode der kleinsten Quadrate
    w = np.linalg.inv(X.T @ X) @ X.T @ y
    return w

gewichte = berechne_trennlinie(daten)

# d) Parameter speichern
np.savetxt('trennlinie_parameter.txt', gewichte)

# Visualisierung
def visualisiere_daten_und_trennlinie(daten, gewichte):
    # Datenpunkte plotten
    fig, ax = plt.subplots()
    farben = {'Kartoffel': 'red', 'Weizen': 'blue'}
    for pflanze in daten['Pflanzenart'].unique():
        subset = daten[daten['Pflanzenart'] == pflanze]
        ax.scatter(subset['x-Koordinate'], subset['y-Koordinate'], 
                   c=farben[pflanze], label=pflanze)
    
    # Trennlinie plotten
    x_values = np.array(ax.get_xlim())
    y_values = -(gewichte[1] * x_values + gewichte[0]) / gewichte[2]
    ax.plot(x_values, y_values, label='Trennlinie', color='green')
    
    # Diagramm beschriften
    ax.set_xlabel('x-Koordinate')
    ax.set_ylabel('y-Koordinate')
    ax.legend()
    plt.title('Klassifizierung der Pflanzenarten')
    plt.show()

visualisiere_daten_und_trennlinie(daten, gewichte)
