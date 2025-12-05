# Ejemplo de Encapsulación aplicado al clima

class SensorClima:
    def __init__(self, temperatura):
        self.__temperatura = temperatura  # Atributo privado

    # Método para ver la temperatura
    def obtener_temperatura(self):
        return self.__temperatura

    # Validamos antes de actualizar
    def actualizar_temperatura(self, nueva_temp):
        if -50 <= nueva_temp <= 50:
            self.__temperatura = nueva_temp
        else:
            print("Temperatura fuera de rango permitido.")

# Uso del encapsulamiento
sensor = SensorClima(25)
print("Temperatura actual:", sensor.obtener_temperatura())
# Actualizamos a un valor válido
sensor.actualizar_temperatura(32)
print("Temperatura actualizada:", sensor.obtener_temperatura())
# Agregamos un valor fuera de rango
sensor.actualizar_temperatura(51)  # No permitido
