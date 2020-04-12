#Capitalización compuesta
#Crear una aplicación que trabaje con la ley de capitalización compuesta.

#La capitalización compuesta es una operación financiera que proyecta un capital a un período futuro,
#  donde los intereses se van acumulando al capital para los períodos subsiguientes.

capitalInicial= float(input("Cual es el capital dispuesto a Capitalización compuesta "))
interes = float(input("Cual es el interes anual? "))
años = int(input("A cuantos años se proyecta el capital "))

porcentaje= interes/100

resultado = capitalInicial*((1+porcentaje)**años)
print(resultado) 