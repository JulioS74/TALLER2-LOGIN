
from models.animal import Animal

class Perro(Animal):
    def __init__(self, nombre, raza, peso, edad):
        super().__init__(nombre, peso, edad)
        self._raza = raza
        self.tipo = 'Perro'
    
    def hacer_sonido(self):
        return "¡Guau, Guau!"
    
    def obtener_raza(self):
        return self._raza
    
    def to_dict(self):
        return {
            'nombre': self._nombre,
            'tipo': self.tipo,
            'sonido': self.hacer_sonido()
        }
