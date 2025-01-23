import numpy as np

def erzeuge_ziffern_datensatz():
    """
    Erzeugt einen Datensatz aus 10 handgefertigten 3x3-Matrizen, die die Ziffern 0-9 repräsentieren.
    Gibt eine Liste von Tupeln (Matrix, Ziffer) zurück.
    """
    datensatz = [
        (np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), 0),  # Ziffer 0
        (np.array([[0, 1, 0], [1, 1, 0], [0, 1, 0]]), 1),  # Ziffer 1
        (np.array([[1, 1, 1], [0, 1, 1], [1, 1, 0]]), 2),  # Ziffer 2
        (np.array([[1, 1, 1], [0, 1, 1], [1, 1, 1]]), 3),  # Ziffer 3
        (np.array([[1, 0, 1], [1, 1, 1], [0, 0, 1]]), 4),  # Ziffer 4
        (np.array([[1, 1, 1], [1, 1, 0], [0, 1, 1]]), 5),  # Ziffer 5
        (np.array([[1, 1, 1], [1, 1, 0], [1, 1, 1]]), 6),  # Ziffer 6
        (np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]]), 7),  # Ziffer 7
        (np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 8),  # Ziffer 8
        (np.array([[1, 1, 1], [1, 1, 1], [0, 0, 1]]), 9),  # Ziffer 9
    ]
    return datensatz

def erkenne_ziffer(matrix):
    """
    Erkennt eine Ziffer basierend auf einer einfachen Logik, die Pixelmuster in der Matrix analysiert.
    """
    # Lade den Datensatz mit den Referenzmatrizen
    datensatz = erzeuge_ziffern_datensatz()
    
    # Vergleiche die Eingabematrix mit den Referenzmatrizen
    for referenz_matrix, ziffer in datensatz:
        if np.array_equal(matrix, referenz_matrix):
            return ziffer
    
    return -1  # Rückgabe, falls keine Übereinstimmung gefunden wird

def teste_erkennung():
    """
    Testet die Funktion erkenne_ziffer() mit dem erzeugten Datensatz.
    Gibt für jede Ziffer die erkannte Ziffer aus.
    """
    datensatz = erzeuge_ziffern_datensatz()
    print("Teste Ziffernerkennung:")
    print("-" * 30)
    
    for matrix, ziffer in datensatz:
        erkannte_ziffer = erkenne_ziffer(matrix)
        print(f"Erwartet: {ziffer}, Erkannt: {erkannte_ziffer}")
        print(matrix)
        print("-" * 30)

if __name__ == "__main__":
    teste_erkennung()
