#Series
#Listar los números entre un valor inicial y uno final,
#  con un cierto intervalo. 
# Al final dar la suma de todos los valores listados.
suma = 0
inicial = int(input("Digite el numero inicial: "))
final = int(input("Digite el valor final:"))
intervalo = int(input("Digite el intervalo: "))

for num in range (inicial,final,intervalo):
    print (num)
    suma+= num
print (suma)

