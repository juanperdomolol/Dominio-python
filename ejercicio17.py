#Índice de masa corporal
#Crear una función que calcule el Índice de Masa Corporal (Body Mass Index [BMI]).

def imc(int, float):
    imc = (peso/altura**2)
    return imc

def estado(float):
    if (resultado<18.5):
        print("Esta por debajo del peso")
    elif (resultado>18.5 and resultado<24.9):
        print("Su estado es saludable")
    elif(resultado>25 and resultado<29.9):
        print("Su estado es con sobrepeso")
    elif(resultado>30 and    resultado<39.9):
        print("Su estado es obeso")
    elif(resultado>40):
        print("Usted es una ballena, tiene obesidad morbida")                

if __name__ == "__main__":
    peso = int(input("Digite su peso en kg: "))
    altura = float(input("Digite su altura en metros: "))
    resultado = imc(peso, altura)
    print("Su imc es: ",resultado)
    estado(resultado)