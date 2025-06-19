# import random

# def clave():
#     clave=3344
#     password=int(input("Ingrese su pass :"))
#     while clave!=password:
#         print ("ERORR, clave invalida")
#         password=int(input("Ingrese su pass :"))

#     print("Bienvenido al sistema")

# def ruleta():
#     barril=random.randint(1,6)
#     rul=int(input("Dispare"))

#     while rul!=barril:
#         rul=int(input("Dispare"))
#     print("BANG!!!")

# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese un numero: "))
    # print(n1+n2)

# def suma_arg(n1,n2):
   
#     print(n1+n2)

# def suma_ret():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     return n1+n2
# def suma_ret_arg(n1,n2):
#     return n1+n2

# suma()
# suma_arg(9,8)

# def suma_1000(num):
#     return num+3000
# result=suma_1000(4000)
# print(result)

# def iva(num):
#    return num*1.19
# resultado=iva(2000)
# print(resultado)

def valor(pre,porcentaje):
    pre=int(input("ingrese el valor del producto:"))
    porcentaje=int(input("ingrese el porcentaje del descuento"))
    return pre-(pre*porcentaje/100)

