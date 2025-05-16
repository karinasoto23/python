#nuevo menu recursivo 
#debe tener 3 programas creados anteriormente 
#los programas deben estar en una funcion 
#el menu debe llamar a estos programas 
#y ejecutarlos de manera correcta 
#debe tener la opcion de salir 
# y la opcion por defecto 
import random
def notas():
    cantN=int(input("ingrese la cantidad de notas"))
    suma=0
    for i in range(cantN):
        print(f"ingrese la nota{i+1}")
        nota=float(input)
        suma=suma+nota
    prom=suma/cantN

    print(f"el promedio es{prom}")

    if prom>= 4: 
        print("ud aprobo")
    else :
        print("ud reaprobo")

def limpieza():
    import time
    import random
    platos_sucios=5

    while platos_sucios!=0:
        platos_sucios-=1
        print("Usted ha lavado un plato, quedan", platos_sucios)
        time.sleep(1)

    for i in range(platos_sucios,-1,-1):
        print("Usted ha lavado un plato, quedan", i)
        time.sleep(1)
def azar():
    
    from random import randint
    print("Ingrese 2 digitos")

    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese un numero"))
    while n1>n2:
     print("El segundo numero no puede ser menor")
    n2=int(input("INgrese un numero"))

    numAzar=randint(n1,n2)
    numAzar=random.randint(n1,n2)
    print("▄"*numAzar)

def opcion():
    while True:
        print('''
            1. notas
            2. limpieza
            3. azar
            4. salir
            ''')


        op=int(input("seleccione una opcion"))



        match op:
            case 1: 
                print("notas")
                notas()
            case 2: 
                print("limpieza")
                limpieza()
            case 3: 
                print("azar")
                azar()
            case 4:
                print("saliendo")
                break 
            case _:
                print("opcion no valida")
                break

opcion()

