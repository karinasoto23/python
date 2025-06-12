#uso y ejemplo de listas 
#reverse= para voltear lista 
#control+f=cambio masivo 
#append= agrega dato a final de la lista 
#ultimo numero en una lista -1
#len = retorna la cantidad de elementos que tiene mi lista, retorna la cantidad de elementos que tiene mi objeto 

# frutas=["durazno", "naranja", "manzana", "pera"]
# for fruta in frutas:
#     print(fruta)
nombres=["karina","constanza "]
apellidos=["soto", "muñoz" , ""]
while True:
    print('''
        1. Ingresa un nombre y apellido
        2. Buscar nombre
        3. Mostrar nombres y apellidos
        4. Salir
          ''')
    op=int(input("Seleccione una opcion"))
    match op:
        case 1: 
            persona=input("Ingrese un nombre")
            apellido=input("ingrese un apellido")
            nombres.append(persona)
            apellidos.append(apellido)
            print(nombres)
            print(apellidos)
        case 2:
            nom=input("ingrese un nombre a buscar ")
            if nom in nombres:
                print("El nombre existe")
            else:
                print("El nombre no existe")

        case 3:
            # c=0
            # for nom in nombres:
            #     print(nombres[c], apellidos [c])
            #     c+=1

            for i in range(len[nombres]):
                print(nombres[i], apellidos[i])
            


        case 4:
            print("saliendo")
            break 
        case _:
            print("ingrese un numero valido")


op=(int(input('''Seleccione una opcion
              1.-
              ''')))


