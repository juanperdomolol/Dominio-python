#Longitud de una cadena
#Crear una función que calcule la longitud de una cadena alfanumérica. 
# Crear otra función que dada una cadena devuelva el primer caracter en mayúsculas 
# y el resto en minúsculas. Pasar una palabra por ambas funciones y dar el resultado.

def calcular(cadena):
    longitud= len(cadena) #len toma la longitud de strings, tamaños y asi
    print("La longitud de la cadena es",longitud)

def convertidor(cadena):
   # convertidor= cadena.capitalize
    print(cadena.capitalize()) #capitalize es un metodo para convertir la primera letra en mayusucula

if __name__ == "__main__":
    cadena = str(input("Digite una palabra: "))
    calcular(cadena)
    convertidor(cadena)
