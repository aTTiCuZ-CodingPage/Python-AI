def perzeptron(x1, x2, w1, w2):
    """
    Berechnet die Ausgabe eines Perzeptrons mit zwei Eingängen
    
    Args:
        x1, x2: Eingabewerte (0 oder 1)
        w1, w2: Gewichte für die Eingänge
        
    Returns:
        1 wenn gewichtete Summe > 1, sonst 0
    """
    summe = x1 * w1 + x2 * w2
    # Aktivierungsfunktion
    if summe > 1:
        return 1
    else:
        return 0

def teste_perzeptron(w1, w2):
    """
    Testet das Perzeptron mit allen möglichen Eingabekombinationen
    und gibt eine formatierte Tabelle aus
    """
    print("\nTest des UND-Perzeptrons:")
    print("-" * 30)
    print("x1 | x2 | Ausgabe | Erwartet")
    print("-" * 30)
    
    # Teste alle möglichen Kombinationen
    for x1 in [0, 1]:
        for x2 in [0, 1]:
            ausgabe = perzeptron(x1, x2, w1, w2)
            erwartet = 1 if (x1 == 1 and x2 == 1) else 0
            print(f"{x1}  | {x2}  | {ausgabe}       | {erwartet}")
    print("-" * 30)

# Initialisiere die Gewichte für die UND-Operation
# Für UND müssen beide Eingänge 1 sein, daher wählen wir
# w1 = w2 = 0.6, sodass nur bei x1=x2=1 die Summe > 1 ist
w1 = 0.6
w2 = 0.6

# Teste das Perzeptron
teste_perzeptron(w1, w2)

# Zusätzliche Erklärung der gewählten Gewichte
print("\nErklärung der Gewichte:")
print(f"w1 = {w1}, w2 = {w2}")
print("Diese Gewichte wurden gewählt, weil:")
print("- Bei x1=x2=0: 0*0.6 + 0*0.6 = 0 (< 1) → Ausgabe 0")
print("- Bei x1=1,x2=0: 1*0.6 + 0*0.6 = 0.6 (< 1) → Ausgabe 0")
print("- Bei x1=0,x2=1: 0*0.6 + 1*0.6 = 0.6 (< 1) → Ausgabe 0")
print("- Bei x1=x2=1: 1*0.6 + 1*0.6 = 1.2 (> 1) → Ausgabe 1")