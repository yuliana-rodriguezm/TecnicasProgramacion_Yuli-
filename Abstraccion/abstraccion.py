# Ejemplo de Abstracción aplicado al clima

# La Clase Clima representa lo esencial: una temperatura y un estado general
class Clima:
    def __init__(self, temperatura, estado):
        self.temperatura = temperatura
        self.estado = estado

    # Método que muestra la información del clima
    def mostrar_info(self):
        print(f"La temperatura es {self.temperatura}°C y el clima está {self.estado}.")

clima_hoy = Clima(28, "soleado")

# Mostramos lo esencial del clima
clima_hoy.mostrar_info()
