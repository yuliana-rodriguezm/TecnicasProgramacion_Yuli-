# Ejemplo de Herencia aplicado al clima

class Clima:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    # Método que devuelve solo la temperatura
    def mostrar(self):
        return f"Temperatura: {self.temperatura}°C"

# Clase que hereda de Clima y representa un día soleado
class Soleado(Clima):
    def mostrar(self):
        #reutilizamos el método de la clase base y le agregamos la descripción específica
        return f"{super().mostrar()} - Clima soleado"

# Clase que hereda de Clima y representa un día nublado
class Nublado(Clima):
    def mostrar(self):
        return f"{super().mostrar()} - Clima nublado"

# Clase que hereda de Clima y representa un día lluvioso
class Lluvioso(Clima):
    def mostrar(self):
        return f"{super().mostrar()} - Clima lluvioso"

# Función que decide qué tipo de clima crear según la temperatura obtenida
def obtener_clima(temperatura):
    if temperatura >= 32:
        return Soleado(temperatura)
    elif temperatura >= 20:
        return Nublado(temperatura)
    else:
        return Lluvioso(temperatura)


c1 = obtener_clima(35)
c2 = obtener_clima(25)
c3 = obtener_clima(15)

print(c1.mostrar())
print(c2.mostrar())
print(c3.mostrar())