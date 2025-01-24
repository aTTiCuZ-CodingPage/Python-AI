import os
from PIL import Image

def verarbeite_bilder(ordnerpfad):
    """
    Verarbeitet alle Bilder in einem Ordner.
    :param ordnerpfad: Pfad zum Ordner mit den Bildern
    """
    # Liste der Dateien im Ordner
    bilder_dateien = [f for f in os.listdir(ordnerpfad) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    if not bilder_dateien:
        print("Keine Bilder im Ordner gefunden.")
        return
    
    print(f"{len(bilder_dateien)} Bilder gefunden. Verarbeitung beginnt...\n")
    
    for bilddatei in bilder_dateien:
        bildpfad = os.path.join(ordnerpfad, bilddatei)
        try:
            print(f"Verarbeite Bild: {bilddatei}")
            
            # a) Lade das Bild und wandle es in ein Graustufenbild um
            bild = Image.open(bildpfad).convert("L")
            
            # b) Ändere die Größe auf 28x28 Pixel
            bild = bild.resize((28, 28))
            
            # c) Erstelle eine Liste aller Pixelwerte
            pixelwerte = list(bild.getdata())
            
            # d) Zähle Pixel mit einer Helligkeit über 200
            helle_pixel = sum(1 for pixel in pixelwerte if pixel > 200)
            
            print(f"  -> Anzahl der Pixel mit einer Helligkeit über 200: {helle_pixel}")
            
            # Optional: Speichere das verarbeitete Bild
            # verarbeiteter_bildpfad = os.path.join(ordnerpfad, f"verarbeitet_{bilddatei}")
            # bild.save(verarbeiteter_bildpfad)
            # print(f"  -> Verarbeitetes Bild gespeichert unter: {verarbeiteter_bildpfad}\n")
        except Exception as e:
            print(f"Fehler beim Verarbeiten von {bilddatei}: {e}")

# Ordnerpfad zu den Bildern (ersetzen durch den tatsächlichen Pfad)
ordnerpfad = "bilder/"  # Ordner mit den Bildern
verarbeite_bilder(ordnerpfad)
