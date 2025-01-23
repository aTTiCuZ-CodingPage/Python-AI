# reaktion.py
from time import sleep, time #1
from random import uniform
print('Drücke ENTER und warte.')
input() #2
print('Sobald "Los!" erscheint, drücke wieder ENTER.')
wartezeit = uniform(3, 6) #3
sleep(wartezeit) #4
print('Los!')
start = time() #5
input() #6
stop = time() #7
reaktionszeit = round(1000 * (stop - start)) #8
anzahlNeuronen = round(reaktionszeit / 2) #9
print('Reaktionszeit:', reaktionszeit, 'Millisekunden') #10
print('An deiner Reaktion waren ungefähr',
      anzahlNeuronen, 'Neuronenschichten beteiligt.')