# Calcular el puntaje de credito
# De bede calcular que tanto credito tiene una persona
# en cierta entidad financiera, debera considerar
# cantidad de ingresos, nivel educacional y nacionalidad
# Cantidad de ingresos
# 500.000 a 1.000.000 : 300.000
# 1.000.000 a 1.500.000: 650.000
# 1.500.001 o mas : 1.000.000
# Nivel Educacional 
# Basico : x1, medio: x1.3 , superior: x1.5
# Nacionalidad 
# Chilena : +300.000, Extranjero: +0

sueldo=int(input("ingrese su sueldo"))
credito=0
if sueldo>=500000 and sueldo<=1000000:
    credito+=300000
elif sueldo>=1000001 and sueldo<=1500000:
    credito+=650000
elif sueldo>=1500001:  
    credito+=1000000
else:
    print("usted no es valido para credito")

print(f"su credito actual es {credito}")

ed=int(input(''' ingrese su nivel educacional
             1. basico 
             2.medio
             3.superior
             '''))
if ed==1:
    credito*=1
elif ed==2:
    credito*=1.3
elif ed==3:
    credito*=1.5
print(f"su credito actual es {credito}")

nacional=input("ingrese su nacionalidad").lower
if nacional=="chilena":
    credito+=300000
else: 
    print("no tiene bono por nacionalidad")

print(f"su credito actual es {credito}")

