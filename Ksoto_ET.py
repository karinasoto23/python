productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}


def stock_marca(productos,stock):
    for llave,valor in productos.items():
        print(f'''
            marca:{valor[0]}
            pantalla:{valor[1]}
            RAM:{valor[2]}
            disco:{valor[3]}
            GB de DD:{valor[4]}
            procesador:{valor[5]}
            video:{valor[6]}
            cantidad:{stock[llave][1]}
            precio:{stock[llave][0]}

              ''')

def actprecio(productos,stock):

        op=input("ingrese el precio a actualizar")
        if op in stock:
            while True:
                precionuevo=int(input("ingrese el nuevo precio a actualizar"))
                if precionuevo>0:
                    stock[op][0]=precionuevo
                    print("se actualizo el precio correcto")
                    break
                else:
                    print("ingrese un precio mayor a 0 ")

def mostrar(productos,stock):
    contar+=1
    print("listado de productos")
    for llave,valor in productos.items():
        print(f'''{contar}marca:{valor[0]}
              stock{stock[llave][0]} modelo:{llave}
             ''' )
    contar+=1

def precio(productos,stock):
     for llave,valor in stock.items():
          if precio== valor[0]:
               id=llave
               print(f'''
                    marca:{productos[id][0]}
                    precio:{precio}
                    stock:{stock[id][0]}
                     ''')
              



while True:
    try:
        op=int(input('''
                        *** MENU PRINCIPAL ***
                            1. Stock marca.
                            2. Búsqueda por precio.
                            3. Actualizar precio.
                            4. Salir.'''))
        match op:
                case 1:
                
                  stock_marca(productos,stock)
                        

                case 2:
                  precio(productos,stock)
            
                case 3:
                  actprecio(productos,stock)

                case 4:
                    print("saliendo...")
                    break
                case _:
                    print("ingrese una opcion valida")


    except Exception as e:
        print("invalido",e)


        git config--global user. name 
                            user.email