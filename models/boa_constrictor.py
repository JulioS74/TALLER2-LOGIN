
from models.animal import Animal

class BoaConstrictor(Animal):
    def __init__(self, pais_origen, impuestos, nombre, edad, peso):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos
        self._ratones_comidos = 0
        self.tipo = 'Boa Constrictor'

    def hacer_sonido(self):
        return "¡Tsss!"

    def calcular_flete(self):
        return self._peso * 10  # Suponiendo un cálculo arbitrario para el flete

    def comer_raton(self):
        if self._ratones_comidos < 10:
            self._ratones_comidos += 1
        else:
            raise ValueError("¡Demasiados Ratones!")

    def dar_ratones_comidos(self):
        return self._ratones_comidos
    
    def to_dict(self):
        return {
            'nombre': self._nombre,
            'tipo': self.tipo,
            'sonido': self.hacer_sonido()
        }
