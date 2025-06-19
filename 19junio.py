# 
frutas= {"manzana:1200", 
        "kiwi: 1500",
        "platano:1000"}
while True:
    try: 
        print('''
            1. Ingresar fruta
            2. Mostrar fruta 
            3. Actualizar precio 
            4. Eliminar fruta
            5. Salir 
              ''')
        op=int(input("Selecciona una opcion"))
        match op: 
            case 1: 
                fruta=input("Ingresar una fruta")
                precio=int(input("Ingrese el precio"))
                frutas[fruta]=precio
            case 2: 
                for key,dato in frutas.items():
                    print(key, "$", dato)
            case 3: 
                for key, dato in frutas.items():
                    print(key,"$", dato)
                fru=input("Cual es la fruta cuyo precio desea actualizar? ")
                if fru in frutas:
                    precio=int(input("Ingrese el precio nuevo: "))
                    frutas[fru]=precio
                else:
                    print("El articulo no existe")

            case 4: 
                for key, dato in frutas.items():
                    print(key,"$", dato)
                borrar=input("Cual es la fruta que desea borrar? ")
                del frutas[borrar]
                print(f"La fruta {borrar} fue borrada")

            case 5:
                print("saliendo...")
            case _:
                print("opcion no valida") 



    except Exception as e:
        print("El error es", e)
