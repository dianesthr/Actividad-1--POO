# Ejercicio 12 - Trabajador

nom = input("Ingrese el nombre del trabajador: ")
nht = float(input("Ingrese el número de horas trabajadas: "))
vhn = float(input("Ingrese el valor de una hora: "))

salario_bruto = nht * vhn
retencion = salario_bruto * 0.125
salario_neto = salario_bruto - retencion

print("EL TRABAJADOR:", nom)
print("SALARIO BRUTO: $", salario_bruto)
print("RETENCIÓN EN LA FUENTE: $", retencion)
print("SALARIO NETO: $", salario_neto)
