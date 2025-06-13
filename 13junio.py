#
productos=["Shampoo", "Jabon", "Crema"]
carrito=[]
precios=[3500, 2000, 4000]
while True:
    while True:
        try:

            print('''Seleccione una opcion
            1.- Agregar productos 
            2.- Comprar 
            3.- Crear boleta 
            4.-Salir
                ''')
            op=int(input("Seleccione una opcion"))
            break
        except Exception:
            print("Ingresa un  numero valido")
            match op:
                case 1:
                    prod=input("Ingrese un producto")
                    productos.append(prod)
                    pre=int(input("ingrese el precio"))
                    precios.append(pre)

                case 2:
                    for i in range(len(productos)):
                        print(i+1, productos[i], "$",precios[i])
                    producto=int(input("Seleccione una opcion"))
                    carrito.append(producto-1)
                    print(carrito)

                case 3: 
                    total=0
                    print('''-------------------------
                            Articulos de limpieza
                          ''')
                    for i in carrito:
                        print(productos[i], "$",precios[i])
                        total=total+precio[i]
                    print("La cantidad de articulos que lleva es", len(carrito))
                    print("El total neto es ", total)
                    print("El total mas IVA es ", total*1.19)


                   
                case 4:
                    print("Saliendo")
                    break
                case _: 
                    print("Opcion invalida")