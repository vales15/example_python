accion_uno = "Ya estoy en la entrada del evento"
accion_dos = "me estoy registrando"

#estructura de control(conditional if o si)
#permite continuar un flujo (Realizar) ¿i se cumple una condicion 
# y en caso de no cumplirse,se puede o no continuar con otro flujo (hacer otra cosa)
# esta secuencia (condicional if ) va acompañado de los operadoers de comparacion
"""
if  estructura_Datos_uno < estructura_Datos_Dos
if  estructura_Datos_uno <= estructura_Datos_Dos
if  estructura_Datos_uno > estructura_Datos_Dos
if  estructura_Datos_uno >= estructura_Datos_Dos
if  estructura_Datos_uno == estructura_Datos_Dos
if  estructura_Datos_uno != estructura_Datos_Dos
"""
#hay variaas maneras de utilizar la sentencia  if
#if simple,if compuesto,if anidado
dato_comparacion = 18 
edad =20

if edad >= dato_comparacion:
    print("Ingresar,disfrutar del evento")

    #if compuesto
"""
if edad >= dato_comparacion:
    print("ingresar,disfrutar del evento")
else:
    print("No ingresar")
"""
"""
boleta= True
fecha_evento = "27-02-2023"
fecha_comparacion = "28-02-2023"
#if aninado
if edad >= dato_comparacion and boleta and fecha_evento == fecha_comparacion:
    print("ingresar;disfrutar del evento")
else:
    print("no ingresar")

"""
"""
LOCALIDADES_DISPONIBLES = "Las localidades disponibles son:"
localidades = "VIP,PREFERENCIAL,GENERAL,BAJA"
print(LOCALIDADES_DISPONIBLES)
print(localidades)

print("Valor de la boleta elegida:")
localidad =2
if localidad == 1:
	print('VIP = 500.000')
if localidad == 2:
	print('	Prefencial = 400.000')
if localidad == 3:
	print('General = 200.000')
if localidad == 4:
	print('Baja = 100.000')
if localidad < 1 or localidad > 4:
	print('error')

switch_semana = {
	1: vip,
	2: preferencial,
	3: general,
	4: baja
}
"""
