import numpy as np
import matplotlib.pyplot as plt

# Setze einen Seed für reproduzierbare Ergebnisse
np.random.seed(42)

# Generiere 100 normalverteilte Zufallszahlen
# mu = 100 (Mittelwert)
# sigma = 15 (Standardabweichung)
iq_werte = np.random.normal(loc=100, scale=15, size=100)

# Runde auf ganze Zahlen
iq_werte = np.round(iq_werte)

# Erstelle ein Histogramm
plt.figure(figsize=(10, 6))
plt.hist(iq_werte, bins=20, edgecolor='black')
plt.title('Verteilung der IQ-Werte')
plt.xlabel('IQ')
plt.ylabel('Häufigkeit')
plt.grid(True)

# Zeige die ersten 10 Werte
print("Die ersten 10 generierten IQ-Werte:")
print(iq_werte[:10].astype(int))

# Berechne einige statistische Kennwerte
print("\nStatistische Kennwerte:")
print(f"Mittelwert: {np.mean(iq_werte):.2f}")
print(f"Standardabweichung: {np.std(iq_werte):.2f}")
print(f"Minimum: {int(np.min(iq_werte))}")
print(f"Maximum: {int(np.max(iq_werte))}")

plt.show()