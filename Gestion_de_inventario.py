#Se crea la lista que guardará los objetos
inventario = []
#Función para agregar productos
def agregar():
#Ciclo while para repetir la función en caso de que el usuario desee agregar más de un producto
    agregar_mas = "si"
    while agregar_mas.lower().strip() == "si":
        nombre_producto = input("Ingrese el nombre del producto: ")
#Ciclo while con try para hacer que el usuario ingrese un entero y no un tipo de valor diferente
        while True:
            try:
                precio_producto = int(input("Ingrese el precio del producto: "))
#Ciclo while con try para hacer que el usuario ingrese un entero y no un tipo de valor diferente
                while True:
                    try:
                        unidades_producto = int(input("Ingrese las unidades del producto: "))
                        break
                    except:
                        print("El valor ingresado no es un número")
                break
            except:
                print("El valor ingresado no es un número")
        valores_inventario = {"nombre" : nombre_producto, "precio" : precio_producto, "unidades" : unidades_producto }
        inventario.append(valores_inventario)
#Ciclo while para hacer que el usuario ingrese si o no 
        while True:
            agregar_mas = input("¿Desea agregar más productos? (si/no): ").lower().strip()
            if agregar_mas == "si":
                pass
                break
            elif agregar_mas == "no":
                break
            else:
                print("Ingrese un valor válido (si/no)")
#If-elif-else, presentan opciones en caso de querer continuar, salirse del menú o en caso de ingresar un valor inválido
    volver_menu = input("¿Desea volver al menú? (si/no) ")
    if volver_menu == "si":
        menu()
    elif volver_menu == "no":
        print("Saliendo...")
    else:
        print("Valor no permitido, redirigiendo al menú...")
        menu()




#Función para consultar productos
def consultar():
#Ciclo while para repetir la función en caso de que el usuario desee consultar otro producto
    consultar_mas = "si"
    while consultar_mas == "si":
        consulta_usuario = input("Ingrese el nombre del producto: ")
        for valor in inventario:
            if valor["nombre"] == consulta_usuario:
                print(f"Nombre: {consulta_usuario}")
                print(f"Precio: {valor["precio"]}")
                print(f"Unidades: {valor["unidades"]}")
                break
        else:
            print("El producto ingresado no está en el inventario")
#Ciclo while para hacer que el usuario ingrese si o no 
        while True:
            consultar_mas = input("¿Desea consultar más productos? (si/no): ")
            if consultar_mas == "si":
                pass
                break
            elif consultar_mas == "no":
                break
            else:
                print("Ingrese un valor válido (si/no)")
#If-elif-else, presentan opciones en caso de querer continuar, salirse del menú o en caso de ingresar un valor inválido
    volver_menu = input("¿Desea volver al menú? (si/no) ")
    if volver_menu == "si":
        menu()
    elif volver_menu == "no":
        print("Saliendo...")
    else:
        print("Valor no permitido, redirigiendo al menú...")
        menu()
        




#Función para actualizar el inventario
def actualizar():
#Ciclo while para repetir la función en caso de que el usuario desee actualizar otro producto
    actualizar_mas = "si"
    while actualizar_mas == "si":
        producto_actualizar = input("Ingrese el nombre del producto: ")
        for valor in inventario:
            if valor["nombre"] == producto_actualizar:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                valor["precio"] = nuevo_precio
                print(f"""Información actualizada:
                        Producto: {producto_actualizar}
                        precio: {nuevo_precio} """)
                break
        else:
            print("El producto ingresado no está en el inventario")
#Ciclo while para hacer que el usuario ingrese si o no 
        while True:
            actualizar_mas = input("¿Desea actualizar más productos? (si/no): ").lower().strip()
            if actualizar_mas == "si":
                pass
                break
            elif actualizar_mas == "no":
                break
            else:
                print("Ingrese un valor válido (si/no)")
#If-elif-else, presentan opciones en caso de querer continuar, salirse del menú o en caso de ingresar un valor inválido
    volver_menu = input("¿Desea volver al menú? (si/no) ")
    if volver_menu == "si":
        menu()
    elif volver_menu == "no":
        print("Saliendo...")
    else:
        print("Valor no permitido, redirigiendo al menú...")
        menu()
    




#Función para Eliminar:
def eliminar():
#Ciclo while para repetir la función en caso de que el usuario desee eliminar otro producto
    eliminar_mas = "si"
    while eliminar_mas == "si":
        producto_eliminar = input("Ingrese el nombre del producto: ")
        for valor in inventario:
            if valor["nombre"] == producto_eliminar:
                inventario.remove(valor)
                print("El producto ha sido eliminado")
                print(f"Lista actualizada: {inventario} ")
                break
        else:
            print("El producto ingresado no está en el inventario")
#Ciclo while para hacer que el usuario ingrese si o no 
        while True:
            eliminar_mas = input("¿Desea eliminar más productos? (si/no): ")
            if eliminar_mas == "si":
                pass
                break
            elif eliminar_mas == "no":
                break
            else:
                print("Ingrese un valor válido (si/no)")
#If-elif-else, presentan opciones en caso de querer continuar, salirse del menú o en caso de ingresar un valor inválido
    volver_menu = input("¿Desea volver al menú? (si/no) ")
    if volver_menu == "si":
        menu()
    elif volver_menu == "no":
        print("Saliendo...")
    else:
        print("Valor no permitido, redirigiendo al menú...")
        menu()





#Función para calcular el valor total de los productos
def valor_total():
    total = sum(map(lambda producto : producto["precio"] * producto["unidades"], inventario))
    print(f"El valor total de su inventario es {total}")
#If-elif-else, presentan opciones en caso de querer continuar, salirse del menú o en caso de ingresar un valor inválido
    volver_menu = input("¿Desea volver al menú? (si/no) ")
    if volver_menu == "si":
        menu()
    elif volver_menu == "no":
        print("Saliendo...")
    else:
        print("Valor no permitido, redirigiendo al menú...")
        menu()
    



#Menú:
def menu():
    print("***Bienvenido al menú del aplicativo Gestion de inventario *** \nEstas son las opciones: \nOpción 1: agregar \nOpción 2: consultar \nOpción 3: " \
    "actualizar \nOpción 4: eliminar \nOpción 5: valor inventario \nOpción 6: salir del menú ")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        agregar()
    elif opcion == "2":
        consultar()
    elif opcion == "3":
        actualizar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        valor_total()
    elif opcion == "6":
        print("Saliendo...")
    else:
        print("El número ingresado no hace parte del menu")
        menu()

menu()

          




