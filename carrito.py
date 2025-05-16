#crear un menu de carrito con las siguientes opciones
#1. ingresar nombre del usuario , sera mostrado en la boleta , con un saludo
#2. comprar , poner productos para poder comprar con su precio correspondiente ej:producto $1000
#3.sacar boleta , calcular el precio netoy el precio mas iva 
#mostrar totales bonus,mostrar cant de articulos que lleva 
#4.salir
#consideraciones: por lo menos 3 productos, no hya limite de compra, se puede salir en cualquier momento, los montos de los productos son fijos


nombre=input(print("ingrese su nombre"))
print("Bienvenido", nombre)
shampo=2500
jabon=1000
cepillo_de_dientes=1500
total=0
while True:
    print('''Que producto llevara?
        1.-shampoo $2500
        2.-jabon $1000
        3. cepillo de dientes $1500
        4.salir
        ''')

    op=int(input("seleccione una opcion"))

    match op:
                    case 1: 
                        print("shampo")
                        total+=2500
                    
                    case 2: 
                        print("jabon")
                        total+=1000
                    
                    case 3: 
                        print("cepillo de dientes")
                        total+=1500
                    
                    case 4:
                        print("saliendo")
                        break 
                    case _:
                        print("opcion no valida")
                        break
    print("su total neto es" , total)
    print("su total con IVA es: ", total*1.19)     
