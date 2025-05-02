#generar un numero aleatorio entre 1 y 50
#pedir al usuario un numero 
#si ingresa un numero mayor decirle ,
#el numero adivinar es menor 
#si ingresa un numero menor decirle ,
#el numero adivinar es mayor 
#ej numeroAdivinar=20
#si ingresa el 15 debe decir "el numero adivinar es mayor"
#si ingresa el 35 debe decir "el numero adivinar es menor"

import random
numeroAdivinar=random.randint(1,50)
num=int(input("adivine el numero"))

while num!=numeroAdivinar:
    print(numeroAdivinar)
    if num>numeroAdivinar
        print("el numero adivinar es menor")
    else:
         print("el numero adivinar es menor")
    num=int(input("adivine el numero"))
print("le achuntaste!")

