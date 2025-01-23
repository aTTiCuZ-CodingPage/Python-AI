# zeige_ziffer.py
import numpy as np
import matplotlib.pyplot as plt #1

stream = open('mnist_train.csv', 'r') #2
datenliste = stream.readlines() #3
stream.close() #4
datensatz = datenliste[4].split(',') #5
pixel = datensatz[1:] #6
bildArray = np.array(pixel, dtype=int).reshape((28, 28)) #7
plt.imshow(bildArray, cmap='Grays_r') #8
plt.show() #9
