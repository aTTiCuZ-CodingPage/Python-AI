import numpy as np 
def mean_squared_error(actual, predicted): 
    return np.mean((actual - predicted) ** 2)

# Angenommene Daten 
dollar_prices = np.array([250, 300, 100, 80, 120]) 
euro_prices = np.array([210, 252, 84, 67.2, 100.8]) 
# Berechnung der Steigung (Wechselkurs) 
wechselkurs = np.sum((dollar_prices - np.mean(dollar_prices)) * (euro_prices - np.mean(euro_prices))) / np.sum((dollar_prices - np.mean(dollar_prices)) ** 2)
                     
# Berechnung des y-Achsenabschnitts 
intercept = np.mean(euro_prices) - wechselkurs * np.mean(dollar_prices) 
# Vorhersage der Euro-Preise 
predicted_euros = wechselkurs * dollar_prices + intercept 
# Berechnung des MSE 
mse = mean_squared_error(euro_prices, predicted_euros) 
print(f"Der berechnete Wechselkurs ist: {wechselkurs:.2f}") 
print(f"Der mittlere quadratische Fehler ist: {mse:.2f}")


import matplotlib.pyplot as plt 
plt.scatter(dollar_prices, euro_prices, color='blue', label='Tatsächliche Daten') 
plt.plot(dollar_prices, predicted_euros, color='red', label='Regressionslinie') 
plt.xlabel('Preis in Dollar') 
plt.ylabel('Preis in Euro') 
plt.legend() 
plt.show()

# Neue Testdaten 
test_dollar_prices = np.array([200, 150, 50]) 
test_euro_prices = np.array([168, 126, 42]) 
# Vorhersage für Testdaten 
test_predicted_euros = wechselkurs * test_dollar_prices + intercept 
 
# Berechnung des MSE für Testdaten 
test_mse = mean_squared_error(test_euro_prices, test_predicted_euros) 

print(f"Der mittlere quadratische Fehler für die Testdaten ist: {test_mse:.2f}")
