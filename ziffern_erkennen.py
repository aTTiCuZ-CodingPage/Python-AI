import numpy as np
import pickle
from PIL import Image
import os
from typing import List

# Konfiguration für das Netzwerk
I_KNOTEN = 784  # Anzahl Eingabeknoten
H_KNOTEN = 100  # Anzahl verborgene Knoten
O_KNOTEN = 10   # Anzahl Ausgabeknoten

# Gewichte laden
def lade_gewichte(dateipfad: str = 'gewichte.dat'):
    """Lädt die Gewichte für das neuronale Netzwerk."""
    try:
        with open(dateipfad, 'rb') as stream:
            return pickle.load(stream)
    except FileNotFoundError:
        raise FileNotFoundError(f"Die Datei '{dateipfad}' wurde nicht gefunden!")
    except Exception as e:
        raise ValueError(f"Fehler beim Laden der Gewichte: {str(e)}")

wih, who = lade_gewichte()

def sig(x: np.ndarray) -> np.ndarray:
    """Sigmoid-Aktivierungsfunktion."""
    return 1 / (1 + np.exp(-x))

def bild_lesen(pfad: str) -> np.ndarray:
    """
    Liest ein Bild, skaliert es auf 28x28, wandelt es in Graustufen um
    und normalisiert die Werte.
    """
    try:
        bild = Image.open(pfad).convert('RGB')  # Sicherheitsmaßnahme: Konvertiere zu RGB
        kleines_bild = bild.resize(size=(28, 28))
        sequenz = kleines_bild.getdata()
        graustufen = [255 - sum(pixel) / 3 for pixel in sequenz]
        graustufen = np.array([pixel if pixel > 120 else 0 for pixel in graustufen])
        eingaben_skaliert = (graustufen / 255 * 0.99) + 0.01
        return eingaben_skaliert.reshape(-1, 1)  # Transponiere für Spaltenvektor
    except Exception as e:
        raise ValueError(f"Fehler beim Lesen des Bildes '{pfad}': {str(e)}")

def vorhersagen(i: np.ndarray) -> np.ndarray:
    """
    Führt eine Vorhersage für die Eingaben durch.
    """
    xh = np.dot(wih, i)
    yh = sig(xh)
    xo = np.dot(who, yh)
    return sig(xo)

def verarbeite_bilder_ordner(ordner: str = "bilder") -> None:
    """
    Verarbeitet alle Bilder in einem angegebenen Ordner.
    """
    if not os.path.exists(ordner):
        print(f"Fehler: Der Ordner '{ordner}' wurde nicht gefunden!")
        return
    
    bildformate = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    bilddateien = [f for f in os.listdir(ordner) if f.lower().endswith(bildformate)]
    
    if not bilddateien:
        print(f"Keine Bilddateien im Ordner '{ordner}' gefunden!")
        return

    print(f"Gefundene Bilddateien: {len(bilddateien)}")
    print("-" * 40)
    
    for dateiname in bilddateien:
        try:
            bildpfad = os.path.join(ordner, dateiname)
            i = bild_lesen(bildpfad)
            o = vorhersagen(i)
            ziffer = np.argmax(o)
            print(f"Datei: {dateiname} -> Erkannte Ziffer: {ziffer}")
        except Exception as e:
            print(f"Fehler bei Verarbeitung von {dateiname}: {str(e)}")
    
    print("-" * 40)
    print("Verarbeitung abgeschlossen!")

if __name__ == "__main__":
    verarbeite_bilder_ordner()
