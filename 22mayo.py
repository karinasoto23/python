#perros de caza 
#pida al usuario la cantidad de perros 
#muestre cual es la couta minima de conejos 
#luego consulte cuantos conejos trajo 
#si el perro trajo la cantidad minima , cumplio la cuota, si no , se queda sin filetes 
#mostrar resumen de perro que cumplieron y los que no 
import random

cuota=4
cumplieron=0
no_cumplieron=0
conejost=0
while True: 
    try:
        perros=int(input("cuantos perros de caza tiene?"))
        break
    except Exception:
        print("solo se permiten numeros enteros")


for perro in range(perros):
    conejos=random.randint(0,10)
    conejost+=conejos
    print(f"el perro {perro+1} trajo {conejos} conejos")
    if conejos>=cuota:
        print("tiene filete")
        cumplieron+=1
    else: 
        print("el perro no recibe filete")
        no_cumplieron+=1


print("los perros que cumplieron son" , cumplieron)
print("los perros que no cumplieron son" , no_cumplieron)  #podria ponerse perros-cumplieron y asi no se pone esta variable 
print("la cantidad de conejos totales fue" , conejost)






