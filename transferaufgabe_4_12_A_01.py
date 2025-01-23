import numpy as np

# a) Definition der Perzeptron-Funktion
def perzeptron(inputs, weights, threshold):
    """
    Perzeptron-Funktion zur Berechnung der Ausgabe.
    inputs: Tuple mit Eingabewerten (z. B. Wahrheitswerte 0 oder 1)
    weights: Liste der Gewichte
    threshold: Schwellenwert für die Aktivierung
    """
    weighted_sum = np.dot(inputs, weights)
    return 1 if weighted_sum > threshold else 0


# b) Initialisierung der Gewichte und Schwellenwert
weights = [0.0, 0.0]  # Startgewichte
threshold = 0.5       # Schwellenwert
learning_rate = 0.1   # Lernrate


# c) Datensatz für die UND-Wahrheitstabelle
# Wahrheitswerte (Eingaben) und erwartete Ausgaben
dataset = [
    ((0, 0), 0), 
    ((0, 1), 0), 
    ((1, 0), 0), 
    ((1, 1), 1),
    ((0, 0), 0),  # Wiederholte Einträge zur Verstärkung
    ((1, 1), 1)
]


# d) Trainingsschleife
def train_perzeptron(dataset, weights, threshold, learning_rate):
    """
    Trainingsfunktion für das Perzeptron.
    dataset: Liste von Eingaben und erwarteten Ausgaben
    weights: Liste der Gewichte
    threshold: Schwellenwert für die Aktivierung
    learning_rate: Lernrate zur Anpassung der Gewichte
    """
    trained = False
    while not trained:
        trained = True  # Annahme, dass das Training abgeschlossen ist
        for inputs, expected in dataset:
            prediction = perzeptron(inputs, weights, threshold)
            error = expected - prediction
            if error != 0:
                # Update der Gewichte basierend auf dem Fehler
                weights[0] += learning_rate * error * inputs[0]
                weights[1] += learning_rate * error * inputs[1]
                trained = False  # Training ist noch nicht abgeschlossen
    return weights


# Training des Perzeptrons
weights = train_perzeptron(dataset, weights, threshold, learning_rate)


# e) Testen des trainierten Perzeptrons
test_data = [
    (0, 0), 
    (0, 1), 
    (1, 0), 
    (1, 1)
]

print("Testergebnisse:")
for inputs in test_data:
    output = perzeptron(inputs, weights, threshold)
    print(f"Eingaben: {inputs}, Ausgabe: {output}")


# f) Diskussion über XOR und Limitierungen des Perzeptrons
"""
Das Perzeptron kann die XOR-Operation nicht erlernen, da diese Operation nicht linear separierbar ist.
Die Funktion XOR hat zwei "1"-Ausgaben (bei (0,1) und (1,0)), die sich diagonal im 2D-Raum befinden.
Ein einfaches Perzeptron zieht eine lineare Grenze (Hyperplane) im Eingaberaum, was bedeutet, dass es
keine Möglichkeit gibt, diese zwei Ausgabeklassen mit einer einzigen Linie zu trennen.

Lösungsansätze:
1. Mehrschichtige neuronale Netze (Multi-Layer Perceptrons, MLPs) mit einer versteckten Schicht
   können nicht-linear separierbare Aufgaben lösen. Die Verwendung von Aktivierungsfunktionen wie
   Sigmoid oder ReLU erlaubt komplexe Transformationen des Eingaberaums.
2. XOR-Operation erfordert mindestens eine Zwischenschicht mit mehreren Neuronen, um eine nicht-lineare
   Trennlinie zu lernen. Dies ist ein Beispiel dafür, warum "Tiefe" in neuronalen Netzen benötigt wird.
"""
