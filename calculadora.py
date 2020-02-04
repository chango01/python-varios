# CREADO POR GITHUB: CHANGO01

# Calculadora estructurada.

def suma(total):                                # Defino las diferentes funciones correspondientes a cada operación.
    valor3=float(input("Ingrese Número: "))   
    total+=valor3
    return total

def resta(total):
    valor3=float(input("Ingrese Número: "))
    total-=valor3
    return total

def multiplicacion(total):
    valor3=float(input("Ingrese Número: "))
    total*=valor3
    return total

def division(total):
    valor3=float(input("Ingrese Número: "))
    if valor3==0:
      valor3=float(input("No se puede dividir por 0, Ingrese nuevo número: "))
      total/=valor3
    else:
      total/=valor3
    return total

loop=True                                               # Creo un while para que se puedan realizar
total=float(input("\nIngrese Número: "))                # operaciones que llaman a las funciones
while loop==True:                                       # hasta que se use el '=' .
    valor2=input("Ingrese Operador(+,-,*,/,=): ")
    if valor2=="+":
      total=suma(total)
    elif valor2=="-":
      total=resta(total)
    elif valor2=="*":
      total=multiplicacion(total)
    elif valor2=="/":
      total=division(total)
    elif valor2=="=":
      print("\nEl Resultado es: ",total,"\n")
      loop=False
    else:
      print("Error")