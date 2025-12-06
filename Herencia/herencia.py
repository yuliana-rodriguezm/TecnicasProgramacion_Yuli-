# Ejemplo de Herencia aplicado al clima

# Clase padre
class Clima:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    # Método que devuelve solo la temperatura
    def mostrar(self):
        print(f"La temperatura es {self.temperatura}°C")

# Clase hija que hereda lo esencial de la clase clima
class ClimaNublado(Clima):
    # Personalizamos 
    def mostrar(self):
        print(f"La temperatura es {self.temperatura}°C y el día está nublado.")

# Uso
clima = ClimaNublado(19)

# Llamamos al método que fue sobrescrito en la clase hija
clima.mostrar()
