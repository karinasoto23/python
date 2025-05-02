#ruleta rusa 
# barril=random.randint(1,6)
# rul=int(input("adivine el numero"))
# while rul!=barril:
#     rul=int(input("dispare"))
# print("bang")
import random
import time

# j1 = 0
# j2 = 0
# meta = 30
# turno = 1

# while j1 < meta and j2 < meta:
#     if turno % 2 == 0:
#         print("Turno de J1")
#         time.sleep(1)
#         dado = random.randint(1, 6)
#         j1 += dado
#         print(f"El J1 sacó {dado}")
#         print(f"Avanza hasta la casilla {j1}")
#     else:
#         print("Turno de J2")
#         time.sleep(1)
#         dado = random.randint(1, 6)
#         j2 += dado
#         print(f"El J2 sacó {dado}")
#         print(f"Avanza hasta la casilla {j2}")
#     turno += 1

# if j1 > j2:
#     print("El ganador es J1")
# else:
#     print("El ganador es J2")

#la florida 20%, la pintana 30%, pte alto 25%, san joaquin 15%
#grupo familiar: 1>=2%, 2 a 4=>3%, 5 o mas=>4%
#preguntar al usuario en que comuna vive 
#preguntar al usuario con cuantas personas vive 
#el arancel actual es de 200.000 por semestre 
#basados en las respuestas del usuario y en la informacion dada, calcula su descuento 
#ej: 
#ingrese su comuna: la florida 
#ingrese su grupo familiar(numero entero ud incluido): 4
#el total del descuento es 23%
#el total a pagar es $154000


arancel=200000
descuento=0
print('''
    1.La Florida 20%
    2.La Pintana 30%
    3.Puente Alto 25%
    4.San joaquin 15%
    '''    )
comuna=int(input("seleccione la comuna"))

if comuna==1:
    descuento=20
elif comuna==2:
    descuento=30
elif comuna==3:
    descuento=25
elif comuna==4:
    descuento=15
else:
    print("seleccion incorrecta")

grupo=int(input("ingrese grupo familiar (numero entero usted incluido) : "))

if grupo==1:
    descuento=descuento+2
elif grupo<=4 and grupo>=2:
    descuento+=3
elif comuna>=5:
    descuento+=4

else:
    print("seleccion incorrecta")

print("el descuento total es" , descuento)
desc=arancel*descuento/100
total=arancel-desc
print("el total a pagar es $", total )