# Ejemplo de Abstracción aplicado al clima

# La Clase Clima representa lo esencial.
class Clima:

    def __init__(self, estado, temperatura):
        self.estado = estado
        self.temperatura = temperatura

    def describir(self):
        print(f"El clima está {self.estado} con una temperatura de {self.temperatura}°C")

# Crear un objeto
mi_clima = Clima("soleado", 28)
mi_clima.describir()
