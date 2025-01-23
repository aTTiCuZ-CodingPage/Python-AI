import matplotlib.pyplot as plt

LR = 0.2
DATEN = [(77, 135, 'M'), (88, 55, 'H'), (70, 115, 'M'),
         (50, 85, 'M'), (80, 140, 'M'), (45, 27, 'H'),
         (79, 132, 'M'), (50, 91, 'M'), (45, 80, 'M'),
         (67, 45, 'H')]

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

# Visualisierungsfunktion
def plot_data_and_decision_boundary(data, a):
    # Datenpunkte plotten
    for breite, hoehe, label in data:
        if label == 'H':
            plt.scatter(breite, hoehe, color='red', label='Hund' if 'Hund' not in plt.gca().get_legend_handles_labels()[1] else "")
        else:
            plt.scatter(breite, hoehe, color='blue', label='Mensch' if 'Mensch' not in plt.gca().get_legend_handles_labels()[1] else "")

    # Trennlinie plotten
    x_values = [0, 150]
    y_values = [a * x for x in x_values]
    plt.plot(x_values, y_values, color='green', label='Trennlinie')

    # Diagramm beschriften
    plt.xlabel('Breite')
    plt.ylabel('Höhe')
    plt.legend()
    plt.title('Klassifizierung von Mensch und Hund')
    plt.grid(True)
    plt.show()

# Visualisierung aufrufen
plot_data_and_decision_boundary(DATEN, a)

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
