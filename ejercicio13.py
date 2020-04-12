#Adivina el número secreto
#Se genera un número aleatorio entero entre 1 y 100.
#  El usuario debe adivinar el número secreto, diciendo en cada tirada si es mayor o menor.

import random 

numero = random.randint(1,101)
intentos=0

while(True):
    intento = int(input("Digite un numero: "))
    intentos+=1

    if intento <numero:
        print("El numero es mayor al digitado")
    elif intento >numero:
        print("El numero es menor al digitado") 
    else:
        print("Felicidades, encontro el numero {} y lo intento {} veces".format(numero, intentos))
        break       