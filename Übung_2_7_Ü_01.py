import numpy as np
import matplotlib.pyplot as plt

def berechne_linreg_koeffizienten(werbeausgaben, verkaufszahlen):
    # Mittelwerte berechnen
    x_mean = np.mean(werbeausgaben)
    y_mean = np.mean(verkaufszahlen)

    # Steigung a berechnen
    a = np.sum((werbeausgaben - x_mean) * (verkaufszahlen - y_mean)) / np.sum((werbeausgaben - x_mean) ** 2)

    # y-Achsenabschnitt b berechnen
    b = y_mean - a * x_mean

    return a, b

def visualisiere_daten(werbeausgaben, verkaufszahlen, a, b):
    # Datenpunkte plotten
    plt.scatter(werbeausgaben, verkaufszahlen, color='blue', label='Datenpunkte')

    # Regressionsgerade plotten
    x_vals = np.array(werbeausgaben)
    y_vals = a * x_vals + b
    plt.plot(x_vals, y_vals, color='red', label='Regressionsgerade')

    # Achsentitel und Legende
    plt.xlabel('Werbeausgaben (in Tsd. Euro)')
    plt.ylabel('Verkaufszahlen (in Einheiten)')
    plt.title('Lineare Regression: Werbeausgaben vs. Verkaufszahlen')
    plt.legend()

    # Plot anzeigen
    plt.show()

# b) Fiktive Daten definieren
werbeausgaben = [10, 15, 20, 25, 30]  # in Tausend Euro
verkaufszahlen = [100, 150, 200, 250, 300]  # in Einheiten

# c) Koeffizienten berechnen
a, b = berechne_linreg_koeffizienten(werbeausgaben, verkaufszahlen)
print(f"Steigung (a): {a:.2f}")
print(f"Y-Achsenabschnitt (b): {b:.2f}")

# d) Daten visualisieren
visualisiere_daten(werbeausgaben, verkaufszahlen, a, b)
