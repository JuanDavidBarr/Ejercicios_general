#Diseñar un sistema que permita registrar compras de boletos de pasajeros, su destino, equipaje, y calcular el costo total del viaje, 
#asignando un ID único por reserva para hacer seguimiento. El sistema debe validar los límites de peso, aplicar cobros por equipaje y generar un resumen detallado.
sistema_gestion = {}
generador_digitos_ID = 1
#Registro de información
ingreso_adicional = "si"
while ingreso_adicional == "si":
    sistema_gestion["COMP000"+str(generador_digitos_ID)] = {"Nombre" : input("Ingrese el nombre del pasajero: "),
                                                            "Tipo" : input("Ingrese el tipo de viaje: "),
                                                            "Peso" : input("Ingrese peso del equipaje principal: "),
                                                            "Equipaje de mano" : input("¿Lleva equipaje de mano?"),
                                                            "Peso equipaje de mano" : input("Ingrese el peso del equipaje de mano (Si no lleva ingrese N/A)"),
                                                            "Fecha del viaje" : input("Ingrese la fecha de la compra (dd/mm/aa): ") }      
    generador_digitos_ID += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    print(sistema_gestion)
    ingreso_adicional = input("¿Desea seguir ingresando información? (si/no): ")

#total recaudado
cantidad_vuelos_nacionales = 0
cantidad_vuelos_internacionales = 0
contador_valores = 0
for valor in sistema_gestion.values():
    if list(sistema_gestion.values())[contador_valores]["Tipo"] == "internacional":
        cantidad_vuelos_internacionales =+ 1
    else:
        cantidad_vuelos_nacionales += 1
    contador_valores += 1

print(cantidad_vuelos_internacionales)
print(cantidad_vuelos_nacionales)
