# CREADO POR GITHUB: CHANGO01

# Conversor números romanos.

def convertir(numero_romano):           # función que convierte el número romano al mismo valor en naturales.
    if numero_romano=="i":
        valor=1
    elif numero_romano=="v":
        valor=5
    elif numero_romano=="x":
        valor=10
    elif numero_romano=="l":
        valor=50
    elif numero_romano=="c":
        valor=100
    elif numero_romano=="d":
        valor=500
    else:
        valor=1000
    return valor

numero=input("Ingrese Número Romano: ")         # Ingreso del número romano y creo un acumulador.
suma=0

for k in range(len(numero)):                    # Recorro el string del número romano,
    if k==len(numero)-1:                        # Realizo la validación del condicional,                
        valor=convertir(numero[k])              # Convierto el número romano a natural 
        suma+=valor                             # y lo sumo o resto al acumulador dependiendo el valor del número siguiente en el string romano.
    elif numero[k]>=numero[k+1]:
        valor=convertir(numero[k])
        suma+=valor
    elif numero[k]<numero[k+1]:
        valor=convertir(numero[k])
        suma-=valor

print(suma)

        
    
    
    