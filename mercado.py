#informacion general
Nombre = input("Nombre del cliente : ")
Documento = input("Documento cliente : ")
mercado_almuerzos = {
    "Arroz x 10lb" : 50000,
    "Carne x 10lb" : 25000,
    "Frijol x 2k" : 5000,
    "Lentejas x 2k" : 7000,
    "Aceite" : 20000
}
print(mercado_almuerzos)
price = mercado_almuerzos ["Arroz x 10lb"] + mercado_almuerzos [ "Carne x 10lb"] + mercado_almuerzos ["Frijol x 2k" ] + mercado_almuerzos ["Lentejas x 2k"] + mercado_almuerzos ["Aceite"]
print ("Total" ,price)

SALDO_DESCUENTO = 100000
SALDO_TOTAL = 107000
if SALDO_TOTAL <= SALDO_DESCUENTO:
    print("El saldo es menor")
else:
    descuento_compra = 10
    valor_descuento = SALDO_TOTAL - (SALDO_TOTAL * 0.10)
    print("Total con descuento", valor_descuento)

