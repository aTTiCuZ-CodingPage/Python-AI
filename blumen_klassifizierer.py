import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    """
    Lädt die Daten aus der CSV-Datei und trennt sie in Features und Labels
    """
    # Lade die CSV-Datei
    data = pd.read_csv(filename, header=None, 
                      names=['Farbintensität', 'Blütenblattgröße', 'Klasse'])
    
    # Trenne Features und Labels
    X = data[['Farbintensität', 'Blütenblattgröße']].values
    y = data['Klasse'].values
    
    return X, y

def calculate_line_parameters(X, y):
    """
    Berechnet die Parameter m und c für die Trennlinie y = mx + c
    Verwendet einen vereinfachten Ansatz basierend auf den Durchschnittspunkten
    der beiden Klassen
    """
    # Trenne Datenpunkte nach Klassen
    rosen_mask = y == 'Rose'
    tulpen_mask = y == 'Tulpe'
    
    # Berechne Durchschnittspunkte für jede Klasse
    rosen_center = np.mean(X[rosen_mask], axis=0)
    tulpen_center = np.mean(X[tulpen_mask], axis=0)
    
    # Berechne Steigung m
    m = -(tulpen_center[0] - rosen_center[0]) / (tulpen_center[1] - rosen_center[1])
    
    # Berechne Mittelpunkt zwischen den Klassenzentren
    mid_point = (rosen_center + tulpen_center) / 2
    
    # Berechne y-Achsenabschnitt c
    c = mid_point[1] - m * mid_point[0]
    
    return m, c

def classify_flower(farbintensitaet, bluetenblattgroesse, m, c):
    """
    Klassifiziert eine Blume basierend auf ihren Merkmalen
    Returns 'Rose' wenn der Punkt über der Linie liegt, sonst 'Tulpe'
    """
    # Berechne y-Wert auf der Linie für gegebenes x
    y_auf_linie = m * farbintensitaet + c
    
    # Wenn der tatsächliche y-Wert größer ist als y_auf_linie,
    # liegt der Punkt über der Linie (Rose)
    if bluetenblattgroesse >= y_auf_linie:
        return 'Rose'
    else:
        return 'Tulpe'

def visualize_classification(X, y, m, c):
    """
    Visualisiert die Datenpunkte und die Trennlinie
    """
    plt.figure(figsize=(10, 6))
    
    # Plotte Datenpunkte
    for label, marker, color in zip(['Rose', 'Tulpe'], ['o', 's'], ['red', 'blue']):
        mask = y == label
        plt.scatter(X[mask, 0], X[mask, 1], 
                   label=label, marker=marker, c=color)
    
    # Plotte Trennlinie
    x_range = np.array([np.min(X[:, 0]), np.max(X[:, 0])])
    y_range = m * x_range + c
    plt.plot(x_range, y_range, 'g--', label='Trennlinie')
    
    plt.xlabel('Farbintensität')
    plt.ylabel('Blütenblattgröße')
    plt.legend()
    plt.grid(True)
    plt.show()

# Hauptprogramm
if __name__ == "__main__":
    # a) Lade Datensatz
    X, y = load_data('blumen_daten.csv')
    
    # b) Berechne Parameter für Trennlinie
    m, c = calculate_line_parameters(X, y)
    print(f"Gefundene Trennlinie: y = {m:.2f}x + {c:.2f}")
    
    # Visualisiere die Klassifizierung
    visualize_classification(X, y, m, c)
    
    # c) Klassifiziere neue Beispiele
    test_beispiele = [
        (140, 5.5),  # sollte Rose sein
        (200, 4.0)   # sollte Tulpe sein
    ]
    
    print("\nKlassifizierung neuer Beispiele:")
    for farbintensitaet, bluetenblattgroesse in test_beispiele:
        klasse = classify_flower(farbintensitaet, bluetenblattgroesse, m, c)
        print(f"Blume mit Farbintensität {farbintensitaet} und "
              f"Blütenblattgröße {bluetenblattgroesse} cm² "
              f"wurde als {klasse} klassifiziert.")