#Funciones
#Crear una función que calcule el cuadrado de un número. 
#Probar la función con los números entre -10 y +10. 
#Crear otra función que lo único que hace es imprimir al final la frase “Programa finalizado”. Ejecutar ambas funciones.

def cuadrado(numero):
    resultado= numero**2
    print (resultado)

def finalizado():
    print("Programa Finalizado")

numero = int(input("Digite un numero entre -10 y 10 "))
while numero<-11 and numero<11:
    print(cuadrado(numero))
    print(finalizado)