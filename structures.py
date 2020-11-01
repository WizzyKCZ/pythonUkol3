veta = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
veta = veta.lower()

def charFrequency(veta):
    pismena = {}

    for i in veta:
        if i in pismena:
            pismena[i] += 1
        else:
            pismena[i] = 1
    return pismena


print(charFrequency(veta))