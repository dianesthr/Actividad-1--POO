# Ejercicio 4 - Edades

def calcular_alberto(juan):
    return juan * 2 / 3

def calcular_ana(juan):
    return juan * 4 / 3

def calcular_mama(juan, alberto, ana):
    return juan + alberto + ana

print("Ingrese la edad de Juan:")
juan = float(input())

alberto = calcular_alberto(juan)
ana = calcular_ana(juan)
mama = calcular_mama(juan, alberto, ana)

print("La edad de Juan es:", juan)
print("La edad de Alberto es:", alberto)
print("La edad de Ana es:", ana)
print("La edad de la mamá es:", mama)
