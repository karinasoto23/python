#crear menu con categorias 

# while True:
#     print('''
#         seleccione una opcion
#           1.-teclado 
#           2.-monitores
#           3.-audifonos
#           4.-pagar
#           5.-salir
#           ''')
    
#     op=int(input())
#     match op:
#         case 1:
#              print('''
#         seleccione una opcion
#           1.-teclado 
#           2.-monitores
#           3.-audifonos
#           4.-pagar
#           5.-salir
#           ''')
           
#         case 2:
#         case 3:
#         case 4:
#         case 5:
 



# El programa debe tener un menú de opciones de donde se pueda realizar el pago del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.
# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al ingresar datos, validar valores no numéricos y errores inesperados.
# b. Se debe programar mensajes de error específicos para guiar al usuario sobre posibles problemas
# saldo=400000
# while True:
#     print(''' 
#           Elija una opcion:
#         1.-Pago tarjeta de credito
#         2.-Simulacion de compra
#         3.-Salir
#           ''')
#     op=int(input())
#     match op:
#         case 1:
#              while True:
#                 try:
#                   print('''
#                      1: deuda a pagar $100.000
#                      2: ingrese el monto que desea abonar
#                     ''')
#                   op= int(input(""))
#                   match op:
#                     case 1:
#                         if op>=0 and op<=saldo:
#                             print("saldo correcto para pago")
#                     case 2:                    
#                 except Exception:
#                     print("ingrese solo numeros enteros")
#         case 2:
#             while True:

#         case 3: 
#             print("saliendo...")
#             break
#         case _:
#             print("numero invalido")

# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800
# La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un cliente el cuál puede ir agregando Rolls a través de un menú uno por uno con solo 
# seleccionar la opción (1 a 4)
# La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario decida que su pedido está completo.
# Luego de ello, debe preguntar al usuario si posee un código de descuento. En caso de que posea el código, deberá ingresarlo. Si el código ingresado es “soyotaku”, debe realizar un 10% de 
# descuento al total del pedido, en caso contrario enviar el mensaje “código no válido” y dar al usuario la opción de reingresar el código o volver al menú tecleando “X”
# Una vez realizado los pasos anteriores, debe mostrar el detalle del pedido contabilizando el total de productos y la cantidad de cada uno de ellos y si aplica o no el descuento

while True:
    try:
        ('''
        Ingrese el sushi 
        1. Pikachu Roll $4500
        2. Otaku Roll $5000
        3. Pulpo Venenoso Roll $5200
        4. Anguila Eléctrica Roll $4800

        ''')
        
        op=int(input())
        match op:
            case 1:
                total*
            case 1:
            case 1:
            case 1:
            case 1:
            case 3: 
                print("saliendo...")
                break
            case _:
                print("numero invalido")

    except Exception:
        print("Solo numeros enteros")

