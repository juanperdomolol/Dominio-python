#Media de n valores
#Calcular la media de n números.

valores=[]
while True:
    valor= int(input("Digite un numero: "))
    valores.append(int(valor))
    mas= int(input("desea digitar mas numeros? 1.si 2.no "))
    if mas !=1:
        break
print(valores)
    
media = sum(valores)/len(valores)
print (media)

