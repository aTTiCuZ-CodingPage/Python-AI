# waehrungsrechner.py
WECHSELKURS = 0.92  # Wechselkurs von Dollar zu Euro

print('Willkommen zum Währungsrechner!')
print('Geben Sie "exit" ein, um das Programm zu beenden.')

while True:
    eingabe = input('Betrag in Dollar (oder "exit" zum Beenden): ')
    
    if eingabe.lower() == "exit":
        print("Programm beendet. Auf Wiedersehen!")
        break  # Schleife verlassen, wenn der Benutzer "exit" eingibt
    
    try:
        dollars = float(eingabe)  # Eingabe in eine Gleitkommazahl umwandeln
        euros = WECHSELKURS * dollars
        print(f'Wert in Euro: {round(euros, 2)}')  # Ergebnis runden und ausgeben
    except ValueError:
        print('Ungültige Eingabe. Bitte geben Sie eine Zahl ein.')

