# Informacion general del usuario
nombre = input("Ingrese nombre del usuario: ")
documento = input("Ingrese numero de identificacion: ")
moneda_origen = input("Ingrese la moneda origen (USD, EUR, SOL, YUAN o BLV): ")
moneda_destino = input("Ingrese la moneda destino (USD, EUR, SOL, YUAN o BLV): ")
cantidad = float(input("Ingrese la cantidad de dinero a cambiar: "))


# Definir diccionario de monedas con sus valores actuales y porcentajes de intermediación
monedas = {
    "USD": {"valor": 3500, "intermediacion": 0.05},
    "EUR": {"valor": 4200, "intermediacion": 0.08},
    "SOL": {"valor": 5000, "intermediacion": 0.1},
    "YUAN": {"valor": 30, "intermediacion": 0.03},
    "BLV": {"valor": 2800, "intermediacion": 0.06}
}

# Validar que las monedas existen en el diccionario
if moneda_origen not in monedas:
    print("La moneda origen" ,moneda_origen , "no está disponible.")
elif moneda_destino not in monedas:
    print("La moneda destino" , moneda_destino , "no está disponible.")
else:
    # Calcular porcentaje de intermediación y comprobar si supera el 10%
    intermediacion = monedas[moneda_destino]["intermediacion"]
    if intermediacion > 0.1:
        print("El porcentaje de intermediación al cambiar a ", moneda_destino," es del {intermediacion*100}%, lo cual supera el límite del 10%.")
        respuesta = input("¿Desea continuar con el cambio? (SI/NO): ")
        if respuesta != "NO":
            print("Operación cancelada.")
            quit()

    # Calcular cantidad de moneda destino y mostrar resultados
    valor_origen = monedas[moneda_origen]["valor"]
    valor_destino = monedas[moneda_destino]["valor"]
    cantidad_destino = cantidad * valor_origen / valor_destino
    total_intermediacion = cantidad * intermediacion
    total_cambio = cantidad - total_intermediacion

    print("\nNombre completo:" ,nombre)
    print("Número de documento de identidad:", documento)
    print("Moneda origen: " ,moneda_origen)
    print("Moneda destino:",moneda_destino)
    print("Porcentaje de intermediación:", intermediacion*0.1)
    print("Cantidad de dinero a cambiar:", cantidad , moneda_origen)
    print("Cantidad de dinero en:", moneda_destino, cantidad_destino , moneda_destino)
    print("Total intermediación: " , total_intermediacion , "COP")
    print("Total cambio: " , total_cambio , "COP")