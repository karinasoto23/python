#preguntar la cantidad de notas y promediarlas 
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