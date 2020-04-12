#Bisiesto
#Crear una función que dado un año diga si es bisiesto.
#Un año es bisiesto en el calendario Gregoriano, 
# si es divisible entre 4 y no divisible entre 100, y también si es divisible entre 400.

def bisiesto(año):
    if año%4==0:
        if año%100==0:
            if año%400==0:
                print("El año es bisiesto")
            else:
                print("No es un año bisiesto") 
        else:
            print("El año es bisiesto")
    else:
        print("No es un año bisiesto") 


año= int(input("Digite un año para determinar si es bisiesto: "))
bisiesto(año)    


       
