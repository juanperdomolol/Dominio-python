#Número mayor y menor
#Dados dos números decir cuál es mayor, o si ambos son iguales.

def mayor(numero1, numero2):
    if numero1>numero2:
        print("El numero 1 es mayor al numero 2")
    else:
        print("El numero 2 es mayor al numero 1")  



if __name__ =='__main__':
    numero1 = int(input("Digite el primer numero: "))
    numero2 = int(input("Segundo numero: "))
    mayor(numero1,numero2)    
    