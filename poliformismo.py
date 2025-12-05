# Ejemplo de Polimorfismo aplicado al clima

class Clima:
    def alerta(self):
        pass

class Soleado(Clima):
    def alerta(self):
        return "Alerta: día muy soleado, usa protector solar."

class Tormenta(Clima):
    def alerta(self):
        return "Alerta: tormenta fuerte, evita salir."

class VientoFuerte(Clima):
    def alerta(self):
        return "Alerta: ráfagas intensas, asegura objetos sueltos."

def mostrar_alerta(clima):
    print(clima.alerta())

# Lista con diferentes tipos de clima
climas = [Soleado(), Tormenta(), VientoFuerte()]

for c in climas:
    # Por el polimorfismo, cada clase responde con su propio texto
    mostrar_alerta(c)
