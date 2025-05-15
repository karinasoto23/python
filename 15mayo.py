


def suma():
    n1=int(input("ingrese un numero:  "))
    n2=int(input("ingrese un numero:  "))
    print("el resultado de la suma es" , n1+n2)

def resta():
    n1=int(input("ingrese un numero:  "))
    n2=int(input("ingrese un numero:  "))
    print("el resultado de la resta es" , n1-n2)

def multiplicacion():
    n1=int(input("ingrese un numero:  "))
    n2=int(input("ingrese un numero:  "))
    print("el resultado de la multiplicacion es" , n1*n2)
def division():
 try: 
    n1=int(input("ingrese un numero:  "))
    n2=int(input("ingrese un numero:  "))
    print("el resultado de la division es" , n1/n2)
 except ZeroDivisionError as mal:
    print("no se puede dividir por 0", mal )


while True:
    print('''
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5. salir
        ''')


    op=int(input("seleccione una opcion"))



    match op:
        case 1: 
            print("suma")
            suma()
        case 2: 
            print("resta")
            resta()
        case 3: 
            print("multiplicacion")
            multiplicacion()
        case 4: 
            print("division")
            division()
        case 5:
            print("saliendo")
            break 
        case _:
            print("opcion no valida")
            break


