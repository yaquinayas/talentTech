def getUnicasLetras(word):
    listLetras = []
    for letra in word:
        if letra not in listLetras:
            listLetras.append(letra)

    listLetras.sort()
    return listLetras


word = input("Ingrese una palabra: ")
print("Letras únicas: ", getUnicasLetras(word))