import numpy as np

class NeuronalesNetz:
    def __init__(self, lernrate=0.1):
        # Zufällige Initialisierung der Gewichte
        self.gewichte_eingabe_hidden = np.random.uniform(-1, 1, (2, 3))  # 2 Eingaben x 3 Hidden
        self.gewichte_hidden_ausgabe = np.random.uniform(-1, 1, (3, 1))  # 3 Hidden x 1 Ausgabe
        
        # Bias-Terme
        self.bias_hidden = np.random.uniform(-1, 1, (3,))
        self.bias_ausgabe = np.random.uniform(-1, 1, (1,))
        
        self.lernrate = lernrate
    
    def sigmoid(self, x):
        """Sigmoid Aktivierungsfunktion"""
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_ableitung(self, x):
        """Ableitung der Sigmoid-Funktion"""
        return x * (1 - x)
    
    def forward(self, eingabe):
        """Forward Propagation"""
        # Hidden Layer
        self.hidden_eingabe = np.dot(eingabe, self.gewichte_eingabe_hidden) + self.bias_hidden
        self.hidden_ausgabe = self.sigmoid(self.hidden_eingabe)
        
        # Ausgabe Layer
        self.ausgabe_eingabe = np.dot(self.hidden_ausgabe, self.gewichte_hidden_ausgabe) + self.bias_ausgabe
        self.ausgabe = self.sigmoid(self.ausgabe_eingabe)
        
        return self.ausgabe

    def backward(self, eingabe, ziel, ausgabe):
        """Backpropagation"""
        # Fehler im Ausgabe-Layer
        fehler_ausgabe = ziel - ausgabe
        delta_ausgabe = fehler_ausgabe * self.sigmoid_ableitung(ausgabe)
        
        # Fehler im Hidden Layer
        fehler_hidden = np.dot(delta_ausgabe, self.gewichte_hidden_ausgabe.T)
        delta_hidden = fehler_hidden * self.sigmoid_ableitung(self.hidden_ausgabe)
        
        # Gewichte aktualisieren
        # Hidden -> Ausgabe
        self.gewichte_hidden_ausgabe += self.lernrate * np.outer(self.hidden_ausgabe, delta_ausgabe)
        self.bias_ausgabe += self.lernrate * delta_ausgabe
        
        # Eingabe -> Hidden
        self.gewichte_eingabe_hidden += self.lernrate * np.outer(eingabe, delta_hidden)
        self.bias_hidden += self.lernrate * delta_hidden
        
        return np.sum(fehler_ausgabe ** 2)

    def trainiere(self, trainingsdaten, epochen=10000):
        """Training des Netzes"""
        for epoche in range(epochen):
            gesamtfehler = 0
            
            for eingabe, ziel in trainingsdaten:
                # Forward pass
                ausgabe = self.forward(eingabe)
                
                # Backward pass
                fehler = self.backward(eingabe, ziel, ausgabe)
                gesamtfehler += fehler
            
            # Fortschritt alle 1000 Epochen ausgeben
            if epoche % 1000 == 0:
                print(f"Epoche {epoche}: Fehler = {gesamtfehler:.10f}")
            
            # Frühzeitiger Abbruch bei sehr kleinem Fehler
            if gesamtfehler < 0.0001:
                print(f"Training konvergiert nach {epoche} Epochen")
                break

def main():
    # XOR Trainingsdaten erstellen
    trainingsdaten = [
        (np.array([0, 0]), np.array([0])),
        (np.array([0, 1]), np.array([1])),
        (np.array([1, 0]), np.array([1])),
        (np.array([1, 1]), np.array([0]))
    ]
    
    # Netz erstellen und trainieren
    netz = NeuronalesNetz(lernrate=0.1)
    
    print("Start des Trainings...")
    netz.trainiere(trainingsdaten)
    
    # Testen des trainierten Netzes
    print("\nTestergebnisse:")
    print("Eingabe -> Ausgabe (Erwartet)")
    print("-" * 30)
    
    for eingabe, ziel in trainingsdaten:
        ausgabe = netz.forward(eingabe)
        print(f"{eingabe} -> {ausgabe[0]:.4f} ({ziel[0]})")

if __name__ == "__main__":
    main()