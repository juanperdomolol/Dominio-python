

#Progresión geométrica
#Calcular cuantos granos de trigo tendríamos que utilizar 
# si por cada casilla de un tablero de ajedrez pusiéramos un grano en la primera casilla, 
# dos en la segunda, cuatro en la tercera, y así doblando hasta la última.

#contando de que un tablero de ajedrez tiene 64 casillas entonces...


granos= 0

for casilla in range (8*8):
    granos+=2**casilla
    

print("El total de granos que necesitamos es ",granos)    