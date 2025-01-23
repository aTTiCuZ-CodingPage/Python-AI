# daten_lesen.py
stream = open('trainingsdaten.csv')
for zeile in stream:
    datenliste = zeile.split(',')
    print(datenliste)
stream.close()