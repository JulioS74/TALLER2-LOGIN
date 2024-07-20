
from models.animal import Animal

class Huron(Animal):
    def __init__(self, pais_origen, impuestos, nombre, edad, peso):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos
        self.tipo = 'Huron'

    def hacer_sonido(self):
        return "¡Eek Eek!"

    def calcular_flete(self):
        return self._peso * 5.0  # Suponiendo un cálculo arbitrario para el flete
    
    def to_dict(self):
        return {
            'nombre': self._nombre,
            'tipo': self.tipo,
            'sonido': self.hacer_sonido()
        }
