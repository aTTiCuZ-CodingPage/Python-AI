from PIL import Image

# Erstelle ein leeres Graustufenbild (L = 8-bit Graustufen)
bild = Image.new("L", (4, 4))  # Bild mit 4x4 Pixeln
print(list(bild.getdata()))
# Definiere eine Liste von Pixelwerten (16 Pixel insgesamt)
pixelwerte = [
    0, 50, 100, 150,
    200, 250, 200, 150,
    100, 50, 0, 50,
    100, 150, 200, 250
]

# Fülle das Bild mit den neuen Pixelwerten
bild.putdata(pixelwerte)
print(list(bild.getdata()))
