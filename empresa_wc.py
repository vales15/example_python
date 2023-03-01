#INFO. GENERAL
nombre = input("Nombre completo empleado : ")
tipo_proyecto = {
"tipo a" :20000,
"tipo b" :10000,
"tipo c" :5000
}

horas_laborales = 30*8
salario_1 = 1500000
salario = 1200000

#salario mensual
saldo = tipo_proyecto["tipo c"]*horas_laborales

print('Valor mensual: ')
print(salario)

Valor_hora = "El valor por hora: "
print(Valor_hora)
print(tipo_proyecto["tipo c"])


if salario >= salario_1:
    print("El salario es mayor a tope maximo")
else:
    porcentaje_incrementado =6
    valor_porcentaje = tipo_proyecto["tipo c"]*(porcentaje_incrementado/100)
    total = tipo_proyecto["tipo c"] + valor_porcentaje

    print("Valor hora extra: " , total)

    aumento = salario + total * 3
    print("EL sueldo mensual con el incremento es :",aumento)

  


    