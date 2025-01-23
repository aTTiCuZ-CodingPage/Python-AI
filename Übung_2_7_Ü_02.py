import numpy as np
import matplotlib.pyplot as plt

# a) Initialer Wechselkurs
a = 1.0

# b) Funktion zur Aktualisierung des Wechselkurses
def update_wechselkurs(dollar_betrag, euro_betrag, aktueller_wechselkurs, lernrate=0.5):
    # Vorhergesagter Euro-Betrag basierend auf aktuellem Wechselkurs
    vorhergesagter_euro = dollar_betrag * aktueller_wechselkurs
    # Fehlerberechnung
    fehler = euro_betrag - vorhergesagter_euro
    # Aktualisierung des Wechselkurses
    neuer_wechselkurs = aktueller_wechselkurs + lernrate * fehler / dollar_betrag
    return neuer_wechselkurs

# c) Testdaten
dollar_betraege = [50, 75, 20, 100]
euro_betraege = [45, 67.50, 18, 90]

# Aktualisierung des Wechselkurses für jeden Datenpunkt
for dollar, euro in zip(dollar_betraege, euro_betraege):
    a = update_wechselkurs(dollar, euro, a)
    print(f"Aktualisierter Wechselkurs: {a:.4f}")

# d) Visualisierung
# Berechnung der Regressionsgerade
dollar_array = np.array(dollar_betraege)
euro_array = np.array(euro_betraege)
# Vorhergesagte Euro-Werte basierend auf dem finalen Wechselkurs
vorhergesagte_euro = a * dollar_array

# Scatter-Plot der Datenpunkte
plt.scatter(dollar_array, euro_array, color='blue', label='Datenpunkte')
# Plot der Regressionsgerade
plt.plot(dollar_array, vorhergesagte_euro, color='red', label='Regressionsgerade')
# Achsenbeschriftungen und Titel
plt.xlabel('Dollar-Betrag')
plt.ylabel('Euro-Betrag')
plt.title('Aktualisierter Wechselkurs durch lineare Regression')
plt.legend()
# Anzeige des Plots
plt.show()
