# graustufen.py
from PIL import Image

PFAD = 'bilder/zwei.jpg'

bild = Image.open(PFAD)
kleinesBild = bild.resize(size=(28, 28))

sequenz = kleinesBild.getdata()
liste = list(sequenz)

graustufen = [255 - sum(pixel)/3 for pixel in liste] #1
graustufen = [pixel if pixel > 120 else 0 for pixel in graustufen]

neuesBild = Image.new(mode='L', size=(28, 28)) #2
neuesBild.putdata(graustufen) #3
neuesBild.show()