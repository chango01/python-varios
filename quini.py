# CREADO POR GITHUB: CHANGO01

# Sorteo Lotería Quini6: selección de 6 números al azar que van de 0 a 45 inclusive.

import random

lista=[i for i in range(46)]     # Creo lista con los valores.

tradicional=[]                   # Creo listas vacías de los sorteos.
segundaVuelta=[]
revancha=[]
siempreSale=[]

for j in range(6):               # Hago la elección al azar de los números y los agrego a cada lista, repito 6 veces el proceso.
    t=random.choice(lista)
    s=random.choice(lista)
    r=random.choice(lista)
    ss=random.choice(lista)
    tradicional.append(t)
    segundaVuelta.append(s)
    revancha.append(r)
    siempreSale.append(ss)

tradicional.sort()              # Ordeno las listas de menor a mayor
segundaVuelta.sort()
revancha.sort()
siempreSale.sort()

print("Resultado Quini6 Tradicional :",tradicional,     
"\nResultado Quini6 Segunda Vuelta :",segundaVuelta,
"\nResultado Quini6 Revancha :",revancha,
"\nResultado Quini6 Siempre Sale :",siempreSale)    # Muestro el resultado.