#ingrese la cantidad de atletas quer participaran , cada atleta debe hacer un salto alto en el rango de 1.55mtrs y 3.78mtrs 
#los atletas bajo 1.55:no califican , entre 1.56 y 2 bronce, entre 2.1 y 3 plata , 3.1 y mas adamtium 
# import random
# noCalifica=0
# broce=0
# plata=0
# adamtium=0
# record=0

    
# while True:
#     try:
#         atletas=int(input("Ingrese la cantidad de atletas: ")) 
#         break
#     except Exception:
#          print ("Solo numeros enteros")


# for a in range(atletas):
#     salto=random.uniform(1.0,3.78)
#     salto=round(salto,2)
#     print(f"El atleta {a+1} saltó {salto}")
#     if salto>record:
#             record=salto

#     if salto<=1.55:
#         print(f"el atleta {a+1} no califica")
#         noCalifica+=1
#     elif salto>1.56 and salto<=2.0: 
#         print(f"el atleta {a+1} gana una medalla de bronce")
#         broce+=1
#     elif salto>2.1 and salto<=3.0:
#         print(f"el atleta {a+1} gana una medalla de plata")
#         plata+=1
#     else: 
#         print(f"el atleta {a+1} gana una medalla de adamtium")
#         adamtium+=1
# print("los jugadores que ganararon de plata fueron", plata)
# print("los jugadores que ganararon de bronce fueron", broce)
# print("los jugadores que ganararon de plata fueron", adamtium)
# print("los jugadores que no califican son :",noCalifica)
# print("el record actual es :" , record)

  
while True:
    while True:
        try:
            print('''
                Seleccione una opcion
            1.- Comprar
            2.- Generar boleta
            3.- Salir
                ''')
            op=int(input())
            break
        except Exception:
            print("Solo numeros enteros")
    match op:
        case 1:
            while True:
                try:
                    op=int(input('''
                                 seleccione el comics que llevara
                                 1.-comics 1 $1500
                                 2.-comics 2 $2500
                                 3.-comics 3 $3000
                                 4.-salir
                                '''))
                    match op:
                        case 1: 
                            print("lleva el comics 1")
                            total+=1500
                            articulos+=1
                        case 2:
                            print("lleva el comics 2")
                            total+=2500
                            articulos+=1
                        case 3:
                            print("lleva el comics 3")
                            total+=3000
                            articulos+=1
                        case 4: 
                            print("volviendo al menu principal")
                            break
                        case _:
                             print("Opcion INvalida")
                except Exception:
                    print("solo numeros enteros")

        case 2:
            while True:
                print("")
                
        case 3:
        case _:
            print("Opcion INvalida")





        

   