
from flask import Blueprint, jsonify, request
from models.gato import Gato
from models.perro import Perro
from models.huron import Huron
from models.boa_constrictor import BoaConstrictor

animal_bp = Blueprint('animal_bp', __name__)

# Crear algunos objetos de ejemplo
animales = [
    Gato('Miau', 'Persa', 4.5, 2, 'Blanco'),
    Perro('Bobby', 'Labrador', 20.0, 3),
    Huron('Slinky', 0.1, 'Slinky', 1, 0.5),
    BoaConstrictor('Kaa', 0.2, 'Kaa', 4, 15.0)
]

@animal_bp.route('/api/animales', methods=['GET'])
def get_animales():
    tipo = request.args.get('tipo')
    if tipo:
        resultados = [animal.to_dict() for animal in animales if animal.tipo.lower() == tipo.lower()]
    else:
        resultados = [animal.to_dict() for animal in animales]
    
    return jsonify(resultados)

@animal_bp.route('/api/sonidos/<tipo>', methods=['GET'])
def get_sonido(tipo):
    tipo_mapeo = {
        'gato': 'Gato',
        'perro': 'Perro',
        'huron': 'Huron',
        'boa': 'Boa Constrictor'
    }
    
    tipo_normalizado = tipo_mapeo.get(tipo.lower())
    if not tipo_normalizado:
        return jsonify({'error': 'Tipo de animal no encontrado'}), 404

    for animal in animales:
        if animal.tipo == tipo_normalizado:
            return jsonify({'tipo': animal.tipo, 'sonido': animal.hacer_sonido()})
    return jsonify({'error': 'Tipo de animal no encontrado'}), 404
