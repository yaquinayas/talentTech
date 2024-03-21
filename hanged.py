import random

def jugar_ahorcado():
    palabras = ['arbol','silla','armario','mesa','cama','celular','agenda','termo','eucalipto']
    palabra = random.choice(palabras)
    palabra_oculta = ['_'] * len(palabra)
    intentos = 3
    letras_intentadas = []

    while intentos > 0 and '_' in palabra_oculta:
        print('Palabra: ' + ' '.join(palabra_oculta))
        print('Intentos restantes: ' + str(intentos))
        print('Letras intentadas: ' + ', '.join(letras_intentadas))
        letra = input('Ingresa una letra: ').lower()

        if letra in letras_intentadas:
            print('Ya intentaste con esa letra.')
        elif letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
        else:
            intentos -= 1
            letras_intentadas.append(letra)

    if '_' in palabra_oculta:
        print('Perdiste! La palabra era ' + palabra)
    else:
        print('Ganaste! La palabra era ' + palabra)

jugar_ahorcado()