import numpy as np
import matplotlib.pyplot as plt
import pickle
from typing import Tuple, List
import random

class NeuralNetwork:
    def __init__(self, input_nodes: int, hidden_nodes: int, output_nodes: int, learning_rate: float):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate

        # He-Initialisierung
        self.wih = self._init_weights(input_nodes, hidden_nodes)
        self.who = self._init_weights(hidden_nodes, output_nodes)

        # Beste Gewichte für Early Stopping
        self.best_wih = None
        self.best_who = None
        self.best_accuracy = 0

    @staticmethod
    def _init_weights(n_inputs: int, n_outputs: int) -> np.ndarray:
        """He-Initialisierung"""
        limit = np.sqrt(2 / n_inputs)
        return np.random.normal(0, limit, (n_outputs, n_inputs))

    @staticmethod
    def relu(x: np.ndarray) -> np.ndarray:
        """ReLU-Aktivierungsfunktion"""
        return np.maximum(0, x)

    @staticmethod
    def relu_derivative(x: np.ndarray) -> np.ndarray:
        """Ableitung von ReLU"""
        return (x > 0).astype(float)

    def forward(self, inputs: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Forward Pass mit Batch-Normalisierung"""
        self.hidden_inputs = np.dot(self.wih, inputs)
        self.hidden_outputs = self.relu(self.hidden_inputs)
        self.final_inputs = np.dot(self.who, self.hidden_outputs)
        self.final_outputs = self.relu(self.final_inputs)
        return self.hidden_outputs, self.final_outputs

    def train_batch(self, batch: List[Tuple[np.ndarray, np.ndarray]]):
        """Mini-Batch-Training"""
        batch_size = len(batch)
        delta_wih = np.zeros_like(self.wih)
        delta_who = np.zeros_like(self.who)

        for inputs, targets in batch:
            # Forward pass
            hidden_outputs, final_outputs = self.forward(inputs)

            # Fehlerberechnung
            output_errors = targets - final_outputs
            hidden_errors = np.dot(self.who.T, output_errors)

            # Akkumuliere Gewichtsänderungen
            delta_who += self.learning_rate * np.dot(output_errors * self.relu_derivative(self.final_inputs), hidden_outputs.T)
            delta_wih += self.learning_rate * np.dot(hidden_errors * self.relu_derivative(self.hidden_inputs), inputs.T)

        # Aktualisiere Gewichte
        self.who += delta_who / batch_size
        self.wih += delta_wih / batch_size

    def evaluate(self, test_data: List[Tuple[np.ndarray, np.ndarray]]) -> float:
        """Evaluiere die Genauigkeit des Netzwerks"""
        correct = 0
        for inputs, targets in test_data:
            _, outputs = self.forward(inputs)
            predicted = np.argmax(outputs)
            expected = np.argmax(targets)
            if predicted == expected:
                correct += 1
        return correct / len(test_data)

def load_data(path: str, output_nodes: int = 10) -> List[Tuple[np.ndarray, np.ndarray]]:
    """Lade und verarbeite MNIST-Daten"""
    try:
        with open(path, 'r') as stream:
            data_list = stream.readlines()

        data = []
        for line in data_list:
            values = line.split(',')

            # Normalisiere Eingaben
            inputs = np.array(values[1:], dtype=float)
            inputs = (inputs / 255.0 * 0.99) + 0.01

            # One-Hot-Encoding für Targets
            targets = np.zeros(output_nodes) + 0.01
            targets[int(values[0])] = 0.99

            # Forme zu Matrizen
            inputs = np.array(inputs, ndmin=2).T
            targets = np.array(targets, ndmin=2).T

            data.append((inputs, targets))

        return data
    except Exception as e:
        print(f"Fehler beim Laden der Daten: {e}")
        return []

def train_network(network: NeuralNetwork, train_data: List[Tuple[np.ndarray, np.ndarray]], 
                  validation_data: List[Tuple[np.ndarray, np.ndarray]], epochs: int, 
                  batch_size: int = 32, patience: int = 5):
    """Trainiere das Netzwerk mit Early Stopping"""
    patience_counter = 0
    accuracies = []

    for epoch in range(epochs):
        print(f"\nEpoche {epoch + 1}/{epochs}")

        # Mische Trainingsdaten
        random.shuffle(train_data)

        # Training in Batches
        for i in range(0, len(train_data), batch_size):
            batch = train_data[i:i + batch_size]
            network.train_batch(batch)

        # Validierung
        accuracy = network.evaluate(validation_data)
        accuracies.append(accuracy)
        print(f"Validierungsgenauigkeit: {accuracy * 100:.2f}%")

        # Speichere beste Gewichte
        if accuracy > network.best_accuracy:
            network.best_accuracy = accuracy
            network.best_wih = network.wih.copy()
            network.best_who = network.who.copy()
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print("Frühzeitiger Abbruch wegen Early Stopping!")
                break

    # Stelle beste Gewichte wieder her
    network.wih = network.best_wih
    network.who = network.best_who

    # Visualisiere den Trainingsverlauf
    plt.plot(accuracies, label="Validierungsgenauigkeit")
    plt.xlabel("Epoche")
    plt.ylabel("Genauigkeit")
    plt.legend()
    plt.show()

def main():
    # Hyperparameter
    INPUT_NODES = 784
    HIDDEN_NODES = 500
    OUTPUT_NODES = 10
    LEARNING_RATE = 0.01
    EPOCHS = 20
    BATCH_SIZE = 32
    PATIENCE = 5

    # Lade Daten
    print("Lade Trainingsdaten...")
    train_data = load_data('mnist_train.csv')
    if not train_data:
        return

    print("Lade Testdaten...")
    test_data = load_data('mnist_test.csv')
    if not test_data:
        return

    # Teile Trainingsdaten in Training und Validierung
    split_idx = int(len(train_data) * 0.8)
    validation_data = train_data[split_idx:]
    train_data = train_data[:split_idx]

    # Erstelle und trainiere Netzwerk
    network = NeuralNetwork(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, LEARNING_RATE)

    print("\nStarte Training...")
    train_network(network, train_data, validation_data, EPOCHS, BATCH_SIZE, PATIENCE)

    # Finale Evaluation
    test_accuracy = network.evaluate(test_data)
    print(f"\nFinale Testgenauigkeit: {test_accuracy * 100:.2f}%")

    # Speichere das Modell
    print("\nSpeichere Modell...")
    with open('model.dat', 'wb') as f:
        pickle.dump({
            "wih": network.wih,
            "who": network.who,
            "input_nodes": network.input_nodes,
            "hidden_nodes": network.hidden_nodes,
            "output_nodes": network.output_nodes,
            "learning_rate": network.learning_rate
        }, f)

    print("Training abgeschlossen!")

if __name__ == "__main__":
    main()
