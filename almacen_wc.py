ZAPATOS = "El precio de los zapatos :"
Precio_zapatos = 350000
TENIS = "El precio de los tenis es :"
Precio_tenis = 280000
CAMISETAS = "El precio de las camisetas es :"
Precio_camisetas =175000
JEANS = "El precio de los jeans es :"
Precio_jeans = 200000

print(ZAPATOS)
print(Precio_zapatos)
print(TENIS)
print(Precio_tenis)
print(CAMISETAS)
print(Precio_camisetas)
print(JEANS)
print(Precio_jeans)

SUMA = "La suma de todos los productos es:"
print(SUMA)
sumar = Precio_zapatos + Precio_tenis + Precio_camisetas + Precio_jeans
print(sumar)

PROMEDIO = " Promedio de la venta es :"
print(PROMEDIO)
promedio_venta = (sumar/4)
print(promedio_venta) 

porcentaje = "El total del aumento del jean:"
print(porcentaje)
Porcentaje_jean = Precio_jeans + (Precio_jeans * 0.062)
print(Porcentaje_jean)

porcentaje2 = "Porcentaje total de la disminucio del precio de zapatos :"
print(porcentaje2)
porcentaje_zapatos = Precio_zapatos - (Precio_zapatos * 0.008)
print(porcentaje_zapatos)

precio_final = "El precio final del jean es :"
print(precio_final)
print(Porcentaje_jean)

precio_final2 = "El precio final de los zapatos es :"
print(precio_final2)
print(porcentaje_zapatos)