# Ejercicio 12 - Trabajador

class Trabajador:
    def __init__(self, horas=48, valor_hora=5000, porcentaje_retencion=0.125):
        self.horas = horas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion
        self.salario_bruto = self.calcular_salario_bruto()
        self.retencion = self.calcular_retencion()
        self.salario_neto = self.calcular_salario_neto()

    def calcular_salario_bruto(self):
        return self.horas * self.valor_hora

    def calcular_retencion(self):
        return self.salario_bruto * self.porcentaje_retencion

    def calcular_salario_neto(self):
        return self.salario_bruto - self.retencion

    def mostrar_resultado(self):
        print("Salario bruto:", self.salario_bruto)
        print("Retención en la fuente:", self.retencion)
        print("Salario neto:", self.salario_neto)


# Programa principal
trabajador = Trabajador()
trabajador.mostrar_resultado()
