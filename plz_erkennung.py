import numpy as np
import random

# Referenz-Matrizen für die Ziffern 0-9
REFERENZ_ZIFFERN = {
    0: np.array([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]),
    1: np.array([[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]),
    2: np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]]),
    3: np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]),
    4: np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]),
    5: np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]]),
    6: np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]),
    7: np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]),
    8: np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]]),
    9: np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]),
}

# ANSI-Farbcodes für ein farbige Darstellung in der Ausgabe
ANSI_COLORS = {
    "BOLD": "\033[1m",
    "RED": "\033[91m",
    "CYAN": "\033[96m",
    "RESET": "\033[0m",
}

def extrahiere_postleitzahl(matrizen):
    """    
    Hier wird eine PLZ aus einer Liste von Matrizen extrahiert
    Matrizen: Liste von 5 numpy-Arrays, die Ziffern darstellen
    Rückgabe: PLZ als String.
    """
    postleitzahl = ""
    for matrix in matrizen:
        for ziffer, referenz in REFERENZ_ZIFFERN.items():
            if np.array_equal(matrix, referenz):
                postleitzahl += str(ziffer)
                break
        else:
            postleitzahl += "?"  # Unbekannte Ziffer
    return postleitzahl

def generiere_test_datensatz():
    """
    Hier wird ein Testdatensatz mit 10 zufälligen Postleitzahlen genriert
    :return: Liste von PLZ, jede als Liste von 5 Matrizen
    """
    return [
        [REFERENZ_ZIFFERN[random.randint(0, 9)] for _ in range(5)]
        for _ in range(10)
    ]

def teste_postleitzahl_erkennung_farbig():
    """
    Teste die Funktion zur Postleitzahlenerkennung mit farbiger Darstellung
    """
    datensatz = generiere_test_datensatz()
    print("\nErgebnisse der Postleitzahlenerkennung mit farbigen Matrizen:")
    print("=" * 50)

    for idx, postleitzahl in enumerate(datensatz):
        erkannte_postleitzahl = extrahiere_postleitzahl(postleitzahl)
        print(f"Nr. {idx + 1} | Erkannte Postleitzahl: {erkannte_postleitzahl}")
        print("-" * 50)

        # Matrixblock für die Postleitzahl anzeigen
        for zeilenblock in range(5):  # Jede Zeile in der 5x3-Matrix
            zeile = []
            for matrix in postleitzahl:
                # rot/fetter Text für die 1
                farbige_zeile = "".join(
                    f"{ANSI_COLORS['BOLD']}{ANSI_COLORS['RED']}1{ANSI_COLORS['RESET']}"
                    if pixel == 1
                    else f"{ANSI_COLORS['CYAN']}0{ANSI_COLORS['RESET']}"
                    for pixel in matrix[zeilenblock]
                )
                zeile.append(farbige_zeile)
            print("   ".join(zeile))  # Trennen der Matrizenblöcke mit Abständen
        print("-" * 50)

# Hauptprogramm
if __name__ == "__main__":
    teste_postleitzahl_erkennung_farbig()
