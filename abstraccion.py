# Ejemplo de Abstracción aplicado al clima

from abc import ABC, abstractmethod

class Clima(ABC):
    @abstractmethod
    def descripcion(self):
        # Método que cada tipo de clima deberá escribir a su manera
        pass


# Clima real: soleado
class Soleado(Clima):
    def descripcion(self):
        return "El día está soleado"


# Clima real: lluvioso
class Lluvioso(Clima):
    def descripcion(self):
        return "El día está lluvioso"


# Uso del modelo
c1 = Soleado()
c2 = Lluvioso()

print(c1.descripcion())
print(c2.descripcion())
