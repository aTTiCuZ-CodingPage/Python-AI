# klassifizierer.py
import matplotlib.pyplot as plt

# Lernrate
LR = 0.2

# Trainingsdaten: (Breite, Höhe, Label)
DATEN = [
    (77, 135, 'M'), (88, 55, 'H'), (70, 115, 'M'),
    (50, 85, 'M'), (80, 140, 'M'), (45, 27, 'H'),
    (79, 132, 'M'), (50, 91, 'M'), (45, 80, 'M'),
    (67, 45, 'H')
]

# Training
a = 0.2
for breite, hoehe, label in DATEN:
    if label == 'H':
        t = hoehe + 1
    else:
        t = hoehe - 1
    e = t - a * breite
    da = LR * e / breite
    a += da

# Visualisierung
# Datenpunkte plotten
for breite, hoehe, label in DATEN:
    if label == 'H':
        plt.scatter(breite, hoehe, color='red', label='Hund' if 'Hund' not in plt.gca().get_legend_handles_labels()[1] else "")
    else:
        plt.scatter(breite, hoehe, color='blue', label='Mensch' if 'Mensch' not in plt.gca().get_legend_handles_labels()[1] else "")

# Trennlinie plotten
x_values = [0, 150]
y_values = [0, a * 150]
plt.plot(x_values, y_values, color='green', label='Trennlinie')

# Achsenbeschriftungen und Titel
plt.xlabel('Breite')
plt.ylabel('Höhe')
plt.title('Klassifikation von Hund und Mensch')
plt.legend()
plt.grid(True)

# Diagramm anzeigen
plt.show()

# Vorhersagen
eingabe_breite = input('Breite: ')
while eingabe_breite != '':
    eingabe_hoehe = input('Höhe: ')
    breite = float(eingabe_breite)
    hoehe = float(eingabe_hoehe)
    if hoehe < a * breite:
        print('Hund')
    else:
        print('Mensch')
    eingabe_breite = input('Breite: ')
print('Auf Wiedersehen')
