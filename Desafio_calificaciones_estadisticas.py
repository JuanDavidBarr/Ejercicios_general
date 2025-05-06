#***** Desafio de calificaciones y estadisticas *****
#Desarrolla un programa en Python que gestione una serie de calificaciones y estadísticas de manera interactiva.
#El programa que vas a desarrollar en este entrenamiento debe:

#Determinar el estado de aprobación:
    #Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
    #Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
#Calcular el promedio:
    #Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    #Calcular y mostrar el promedio de las calificaciones en la lista
#Contar calificaciones mayores:
    #Preguntar al usuario por un valor específico
    #Contar cuántas calificaciones en la lista son mayores que este valor
#Verificar y contar calificaciones específicas
    #Preguntar al usuario por una calificación específica. 
    #Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y continue para controlar el flujo del programa. 

#Se crean las funciones que van a ejecutar las diferentes acciones de la aplicación
#1. Estado de aprobación
#Se valida que el valor ingresado sea un número
lista_notas = []
def estado_aprobacion():
    es_numero = None
    while not es_numero:
        try:
            Nota_final = int(input("Ingrese la nota obtenida, (ingrese solo valores entre 1 y 100): "))
    #Se valida que el valor esté en el rango permitido
            if 0 <= Nota_final <= 100:
                es_numero = True
            else:
                print("El valor ingresado no se encuentra dentro del rango permitido. Intente de nuevo")
        except:
            print("Por favor ingrese un valor numérico")
    #Se compara la nota ingresada con el rango de aprobación
    if Nota_final >= 60:
        print("Usted aprobó")
    else:
        print("Usted reprobó")



#2. Calcular promedio
def calcular_promedio():
    global lista_notas
    es_numero = None
    #Se valida que el valor ingresado sea un número
    while not es_numero:
        try:
            cantidad_notas = int(input("Ingrese la cantidad de notas para hayar su promedio: "))
            lista_notas = []
            es_numero = True
            for nota_numero in range(cantidad_notas):
                in_rango = None
                while not in_rango:
                    try:
                        nota = int(input(f"Ingrese la nota {nota_numero + 1}: "))
    #Se valida que el valor esté en el rango permitido
                        if 0 <= nota <= 100:
                            lista_notas.append(nota)
                            in_rango = True
                        else:
                            print("El valor ingresado no se encuentra dentro del rango permitido. Intente de nuevo")
                    except:
                        print("Por favor ingrese un valor numérico")
        except:
            print("Por favor ingrese un valor numérico")
    #Calculamos el promedio sumando todos los elementos de la lista con la función "sum" y dividimos pro la cantidad de elementos usando la función "len"
    promedio_lista_notas = sum(lista_notas) / len(lista_notas)
    print(f"El promedio de notas ingresadas es: {promedio_lista_notas}")



#3. Conteo de calificaciones mayores
def conteo_notas_mayores():
    global lista_notas
    es_numero = None
    #Se valida que el valor ingresado sea un número
    while not es_numero:
        try:
            nota_comparar = int(input("Ingrese la nota que desea comparar: "))
            contador = 0
            veces_mayor = 0
    #Se valida que el valor esté en el rango permitido
            if 0 <= nota_comparar <= 100:
                es_numero = True
    #Se compara cada elemento de la lista con el número ingresado, cada vez que este sea menor al elemento de la lista, se suma a la variable
                while contador < len(lista_notas):
                    if nota_comparar < lista_notas[contador]:
                        veces_mayor += 1
                    contador += 1
                print(f" {veces_mayor} calificaciones son más grandes que el valor ingresado")
            else:
                print("La nota no se encuentra en el rango permitido")
        except:
            print("Por favor ingrese un valor numérico")



#4. Verificación y conteo
def verficacion_conteo():
    global lista_notas
    es_numero = None
    veces_esta = 0
    while not es_numero:
        try:
            nota_verificar = int(input("Ingrese la nota que desea verificar: "))
    #Se valida que el valor esté en el rango permitido
            if 0 <= nota_verificar<= 100:
                es_numero = True
    #Se recorre cada elemento de la lista y se compara con el valor ingresado para ver sin es igual o no. Si es igual, se suma una a la variable que indica cuantas veces está.
                for nota in lista_notas:
                    if nota == nota_verificar:
                        veces_esta += 1
                print(f"La nota {nota_verificar} está {veces_esta} vez/veces en la lista")
            else:
                print("La nota no se encuentra en el rango permitido")
        except:
            print("Por favor ingrese un valor numérico")



#Menú de opciones
def menu_opciones():
    print("""Opciones del menu:
          1. Saber si aprobó o reprobó
          2. Calcular promedio
          3. Verificar notas mayores que la nota ingresada
          4. Verificar número de veces que se repite una nota
          """)
    desea_continuar = "si"
    while desea_continuar.strip().lower() == "si":
        opcion_usuario = input("Ingrese la opción de la acción que desea realizar: ")
        if opcion_usuario == "1":
            estado_aprobacion()
        elif opcion_usuario == "2":
            calcular_promedio()
        elif opcion_usuario == "3":
            conteo_notas_mayores()
        elif opcion_usuario == "4":
            verficacion_conteo()
        else:
            print(f"{opcion_usuario} no se encuentra dentro del menú")

        desea_continuar = input("Desea permancer en el menu? (Si/No): ")

menu_opciones()





    

    
