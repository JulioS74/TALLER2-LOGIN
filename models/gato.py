
from models.animal import Animal

class Gato(Animal):
    def __init__(self, nombre, raza, peso, edad, color):
        super().__init__(nombre, peso, edad)
        self._raza = raza
        self._color = color
        self.tipo = 'Gato'
    
    def hacer_sonido(self):
        return "¡Miau, miau!"
    
    def obtener_color(self):
        return self._color
    
    def to_dict(self):
        return {
            'nombre': self._nombre,
            'tipo': self.tipo,
            'sonido': self.hacer_sonido()
        }
