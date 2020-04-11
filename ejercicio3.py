#Intervalos
#Generar un número aleatorio entre 1 y 120. 
#Decir si se encuentra en el intervalo entre 10 y 50, o bien si es mayor de 50 hasta 100, 
# o bien si es mayor de 100, o bien si es menor de 10.

import random

Aleatorio = random.randrange(1, 120)

if (Aleatorio>10 and Aleatorio<50):
    print("se encuentra en el intervalo entre 10 y 50")
elif (Aleatorio>50 and Aleatorio<100):
    print("se encuentra en el intervalo entre 50 y 100")  
elif (Aleatorio>100 and Aleatorio<=120):
    print("se encuentra en el intervalo entre 100 y 120")    
else: 
    print("El numero es menor de 10")

print("El numero es: ",Aleatorio)