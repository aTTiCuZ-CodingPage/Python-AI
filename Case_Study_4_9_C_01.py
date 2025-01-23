import numpy as np

class Perzeptron:
    def __init__(self, lernrate=0.1):
        self.gewichte = np.random.rand(2)  # Zufällige Initialisierung
        self.bias = np.random.rand()
        self.lernrate = lernrate
        
    def aktivierungsfunktion(self, x):
        return 1 if x > 0 else 0
    
    def vorhersage(self, eingaben):
        summe = np.dot(self.gewichte, eingaben) + self.bias
        return self.aktivierungsfunktion(summe)
    
    def trainiere(self, trainingsdaten, epochen=100):
        """
        Trainiert das Perzeptron mit der Delta-Regel
        """
        for epoche in range(epochen):
            fehler_summe = 0
            for eingabe, erwartung in trainingsdaten:
                # Vorhersage machen
                vorhersage = self.vorhersage(eingabe)
                
                # Fehler berechnen
                fehler = erwartung - vorhersage
                fehler_summe += abs(fehler)
                
                # Gewichte und Bias anpassen (Delta-Regel)
                if fehler != 0:  # Nur anpassen wenn die Vorhersage falsch war
                    self.gewichte += self.lernrate * fehler * np.array(eingabe)
                    self.bias += self.lernrate * fehler
            
            # Optional: Früher aufhören wenn keine Fehler mehr
            if fehler_summe == 0:
                print(f"Training konvergiert nach {epoche + 1} Epochen")
                break

def erstelle_testdaten():
    return [
        ([0.1, 0.7], 1),
        ([0.6, 0.2], 1),
        ([0.4, 0.3], 0),
        ([0.8, 0.1], 1),
        ([0.2, 0.5], 1),
        ([0.0, 0.0], 0),
        ([0.9, 0.9], 1),
        ([0.2, 0.2], 0),
        ([0.3, 0.6], 1),
        ([0.7, 0.4], 1)
    ]

def main():
    perzeptron = Perzeptron(lernrate=0.1)
    testdaten = erstelle_testdaten()
    
    print("Initialer Test vor Training:")
    evaluiere_perzeptron(perzeptron, testdaten)
    
    print("\nStarte Training...")
    perzeptron.trainiere(testdaten)
    
    print("\nTest nach Training:")
    evaluiere_perzeptron(perzeptron, testdaten)
    print(f"Finale Gewichte: {perzeptron.gewichte}")
    print(f"Finaler Bias: {perzeptron.bias}")

def evaluiere_perzeptron(perzeptron, testdaten):
    korrekt = 0
    print("Pixelbereich 1, Pixelbereich 2 -> Vorhersage (Erwartet)")
    print("-" * 60)
    
    for eingabe, erwartung in testdaten:
        vorhersage = perzeptron.vorhersage(eingabe)
        korrekt += (vorhersage == erwartung)
        print(f"[{eingabe[0]:.1f}, {eingabe[1]:.1f}] -> {vorhersage} (Erwartet: {erwartung})")
    
    genauigkeit = korrekt / len(testdaten) * 100
    print(f"\nGenauigkeit: {genauigkeit:.1f}%")

if __name__ == "__main__":
    main()