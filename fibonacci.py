# CREADO POR GITHUB: CHANGO01

# Crear lista de números Fibonacci a partir de un indice, comienza de 1.

def numeros_fibonacci(num):             # Creo la función.
    fibonacci=[]                        # Creo una lista vacia.
    for i in range(num):                # Realizo un for hasta el indice ingresado.
        if i==0:                        # Los primeros dos números son 1 y los agrego a la lista.
            fibonacci.append(1)
        elif i==1:
            fibonacci.append(1)
        else:
            valor=(fibonacci[i-1]+fibonacci[i-2])   # Realizo la resta de los 2 npumeros anteriores para obtener el número siguiente
            fibonacci.append(valor)                 # Lo agrego a la lista.
    return fibonacci
    
num=int(input("Ingrese número: "))
print("Números FIBONACCI: ",numeros_fibonacci(num))





