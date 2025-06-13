#es un conjunto de pares de datos

dic={
    "nombre": "karina",
    "numero": 230895,
    "casado":False,

}

print(dic)

dic["ciudad"]="Santiago"

for key, value in dic.items(): #items como es funcion debe ir con parentesis 
    print(key, value)