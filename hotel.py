#Tarifas hotel
Categoria = {
"individual" : 2500, 
"doble" : 4600,
"familiar" : 5200
}

Categoria2 = {
"individual" : "individual",
"doble" : "doble",
"familiar" : "familiar"
}

#categoria elegida
Categoria1 = (input("Categoria elegida : "))
#proceso hospedaje
dia = int (input("Ingrese cantidad de dias a hospedarse: "))

mul1 = (dia * Categoria["doble"]) + ((Categoria["doble"] * dia) * (16/100))

mul2 = (dia * Categoria["individual"]) + ((Categoria["individual"] * dia) * (16/100))

mul3 = (dia * Categoria["familiar"]) + ((Categoria["familiar"] * dia) * (16/100))

descuento = (mul1 * (5/100))
descuento1 = (mul2 * (9/100))
descuento2 = (mul3 * (15/100))

total = mul1 - descuento
total1 = mul2 - descuento1
total2 = mul3 - descuento2

if Categoria1 == Categoria2 ["doble"]:
    print("el precio total de su estadia en base a su categoria es: ", mul1, ", por tanto tienes un descuento de:", descuento, "valor total", total)
if Categoria1 == Categoria2["individual"]:
    print("el precio total de su estadia en base a su categoria es: ", mul2, ", por tanto tienes un descuento de:", descuento1, "valor total", total1)
if Categoria1 == Categoria2 ["familiar"]:
    print("el precio total de su estadia en base a su categoria es: ", mul3, ", por tanto tienes un descuento de:", descuento2, "valor total", total2)