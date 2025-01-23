def klassifiziere_frucht(breite, hoehe):
    """
    Klassifiziert eine Frucht basierend auf Breite und Höhe.
    
    Args:
    breite (float): Die Breite der Frucht.
    hoehe (float): Die Höhe der Frucht.
    
    Returns:
    str: 'Apfel' oder 'Banane' basierend auf den Abmessungen.
    """
    if breite > 1.2 * hoehe:
        return 'Banane'
    else:
        return 'Apfel'

# Gegebener Datensatz
daten = [
    (8, 8, 'Apfel'),
    (3, 8, 'Banane'),
    (7, 7, 'Apfel'),
    (3, 9, 'Banane'),
    (8, 6, 'Banane'),
    (7, 8, 'Apfel'),
    (8, 7, 'Apfel'),
    (2, 7, 'Banane'),
    (7, 7, 'Apfel'),
    (4, 8, 'Banane')
]

# Testen der Funktion mit neuen Datenpunkten
test_daten = [
    (6, 6),  # Erwartet: Apfel
    (5, 7),  # Erwartet: Apfel
    (9, 5),  # Erwartet: Banane
    (4, 4),  # Erwartet: Apfel
    (10, 7)  # Erwartet: Banane
]

for breite, hoehe in test_daten:
    ergebnis = klassifiziere_frucht(breite, hoehe)
    print(f'Breite: {breite}, Höhe: {hoehe} -> Klassifiziert als: {ergebnis}')
