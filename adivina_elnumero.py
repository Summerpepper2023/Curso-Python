import random

print("Bienvenido, debes adivinar un numero para ganarte un premio")
print("Escoge un numero entre el 1 y el 10")

numero_ganador = random.randit(1, 10)
numero_escogido = int(input("Escoge un numero: "))

if numero_escogido == numero_ganador:
    print("Felicidades has acertado el numero, ganaste unos camina con bendicion ve")

if numero_escogido != numero_ganador:
    print("no bro cagaste, vuelve a intentar :(")
    print("El numero correcto era: {}".format(numero_ganador))