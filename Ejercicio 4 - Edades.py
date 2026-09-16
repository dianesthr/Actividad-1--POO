# Ejercicio 4 - Edades

class Edades:
    def __init__(self, edad_juan):
        self.juan = edad_juan
        self.alberto = self.calcular_alberto()
        self.ana = self.calcular_ana()
        self.mama = self.calcular_mama()

    def calcular_alberto(self):
        return self.juan * 2 / 3

    def calcular_ana(self):
        return self.juan * 4 / 3

    def calcular_mama(self):
        return self.juan + self.alberto + self.ana

    def mostrar_resultado(self):
        print("La edad de Juan es:", self.juan)
        print("La edad de Alberto es:", self.alberto)
        print("La edad de Ana es:", self.ana)
        print("La edad de la mamá es:", self.mama)

# Programa principal
edad_juan = float(input("Ingrese la edad de Juan: "))
edades = Edades(edad_juan)
edades.mostrar_resultado()
