saldo = 0
movimientos = []
while True:
    opcion_usuario = int(input("""Indique la operación que desea realizar: 
            1. consultar el saldo
            2. retirar dinero
            3. depositar dinero
            4. ver_historial
            5. salir
            :    """))
    if opcion_usuario == 1:
        print(f"Su saldo es de {saldo}")

    elif opcion_usuario == 2:
        dinero_retirar = int(input("Ingrese el valor que desea retirar "))
        saldo -= dinero_retirar
        print(f"Nuevo saldo es igual a {saldo}")
        movimientos.append(f"- {dinero_retirar}")

    elif opcion_usuario == 3:
        dinero_depositar = int(input("Ingrese el valor que desea depositar: "))
        saldo += dinero_depositar
        print(saldo)
        print(f"Nuevo saldo es igual a {saldo}")
        movimientos.append(f"+ {dinero_depositar}")

    elif opcion_usuario == 4:
        print("Su historial es")
        for i in movimientos:
            print(i)
        print(f"El saldo total es {saldo}")
    elif opcion_usuario == 5:
        print("Muchas gracias por utilizar nuestros servicios. Vuelva pronto")
    else:
        print("La opción ingresada no se encuentra dentro del menú")



