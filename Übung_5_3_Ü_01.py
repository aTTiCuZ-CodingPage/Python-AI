import numpy as np
import pandas as pd

# a) Definition der Sigmoid-Funktion
def sigmoid(x):
    """
    Berechnet den Wert der Sigmoid-Funktion.
    :param x: Eingabewert
    :return: sig(x)
    """
    return 1 / (1 + np.exp(-x))

# b) Definition der Ableitung der Sigmoid-Funktion
def sigmoid_derivative(x):
    """
    Berechnet den Wert der Ableitung der Sigmoid-Funktion.
    :param x: Eingabewert
    :return: sig'(x)
    """
    sig = sigmoid(x)
    return sig * (1 - sig)

# c) Erstellen des Datensatzes
x_values = np.linspace(-5, 5, 10)  # 10 gleichmäßig verteilte Werte von -5 bis 5

# d) Berechnung und Ausgabe der Tabelle
results = {
    "x": x_values,
    "sigmoid(x)": [sigmoid(x) for x in x_values],
    "sigmoid'(x)": [sigmoid_derivative(x) for x in x_values],
}

# Tabelle mit pandas für eine schöne Darstellung
results_table = pd.DataFrame(results)
print(results_table)
