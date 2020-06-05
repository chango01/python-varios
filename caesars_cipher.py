# CREADO POR GITHUB: CHANGO01

# Generar código  CAESARS CIPHER usando ROT-13.

import re           # Importo re para trabajar con regular expressions.

def cipher(rot_13,palabra_frase):           # Creo función con el diccionario rot_13, y el input como parámetro.
    cifrado=""                              # Creo variable de tipo string vacía.
    for i in palabra_frase:                 # Recorro el input.
        if re.match("[A-Z]",i) is None:     # Pregunto si el carácter del input es distinto a una letra lo agrego a la variable creada.
            cifrado+=i
        else:
            for j in rot_13:                # Y si es igual a una letra, recorro el diccionario rot_13 para agregar el valor que corresponde.
                if i==j:
                    cifrado+=rot_13[j]
    return cifrado
    

rot_13={"A":"N","B":"O","C":"P","D":"Q","E":"R","F":"S","G":"T",        
"H":"U","I":"V","J":"W","K":"X","L":"Y","M":"Z","N":"A","O":"B","P":"C",
"Q":"D","R":"E","S":"F","T":"G","U":"H","V":"I","X":"K","W":"J","Y":"L","Z":"M"}

palabra_frase=input("Ingrese palabra o frase a codificar: ")                # Input a codificar.
print("\nCÓDIGO CAESARS CIPHER: ",cipher(rot_13,palabra_frase.upper()))     