# klassifizierer.py
import matplotlib.pyplot as plt

# Lernrate
LR = 0.2

# etekettierte Trainingsdaten lesen (Breite, Höhe, Label)
DATEN = []
stream = open('trainingsdaten.csv')
for zeile in stream:
    breite, höhe, label = zeile.split(',')
    datentupel = (int(breite), int(höhe), label[0])
    DATEN.append(datentupel)
stream.close()

print(DATEN)

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
