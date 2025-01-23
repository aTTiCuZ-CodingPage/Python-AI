from matplotlib.pyplot import *
from math import e

def sig(x):
    """Sigmoid-Funktion"""
    return 1 / (1 + e**-x)

def sig_derivative(x):
    """Ableitung der Sigmoid-Funktion"""
    # Die Ableitung der Sigmoid-Funktion ist: sig(x) * (1 - sig(x))
    return sig(x) * (1 - sig(x))

# Erzeuge x-Werte von -10 bis +10 in 0.1er Schritten
x_ = [x/10 for x in range(-100, 100)]

# Berechne die y-Werte für beide Funktionen
y_1 = [sig(x) for x in x_]  # Sigmoid-Funktion
y_2 = [sig_derivative(x) for x in x_]  # Ableitung der Sigmoid-Funktion

# Plotte beide Funktionen
plot(x_, y_1, 'b-', label='Sigmoid')  # blau, durchgezogen
plot(x_, y_2, 'r--', label='Ableitung')  # rot, gestrichelt

# Beschriftungen und Layout
xlabel('x')
ylabel('y')
title('Sigmoid-Funktion und ihre Ableitung')
grid()
legend()  # Fügt eine Legende hinzu
show()