# CREADO POR GITHUB: CHANGO01

import re               # importo re para trabajar con "regular expressions".

palabras_frase=input("Ingrese Palabra/Texto para vev si es palindromo: ")      # entrada de la palabra o frase.
x=re.findall("[a-z]",palabras_frase.lower())                 # busco solo las letras(eliminando caracteres especiales, etc,) y las agrego en una lista.

lista=x                     # Creo otra lista y uso el método reverse.
lista.reverse()

x=tuple(x)                  # Convierto en tupla ambas listas para luego poder comparar.
lista=tuple(lista)

if lista==x:                            # Realizo la comparación.
    print(True,"Es palindromo.")
else:
    print(False,"No es palindromo.")
