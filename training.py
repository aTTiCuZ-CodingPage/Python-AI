# training.py
a = 1 #1
eingabeDollars = input('Betrag in Dollar: ') #2
while eingabeDollars != '': #3
    dollars = float(eingabeDollars) #4
    vorhersageEuros = a * dollars
    print('Vorhersage: ', round(vorhersageEuros, 2), '€') #5
    eingabeEuros = input('Tatsächlicher Betrag in Euro: ') #6
    euros = float(eingabeEuros) #7
    fehler = euros - vorhersageEuros #8
    print('Fehler:', fehler)
    a += 0.5 * fehler / dollars #9
    print('Neuer Wechselkurs a:', round(a, 4)) #10
    eingabeDollars = input('Betrag in Dollar: ') #11
print('Auf Wiedersehen!')
