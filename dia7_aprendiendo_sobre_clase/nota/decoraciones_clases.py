# Ejemplo de clase utilizando el decorador @dataclass
from dataclasses import dataclass

@dataclass # <-- Decorador de clase
class Producto:
    nombre: str
    precio: float
    cantidad: int = 0

p1 = Producto("Monitor", 350.0)
print(p1.nombre)

# decoracion @dataclass @classmethod @staticmethod
from dataclasses import dataclass

@dataclass
class Persona:
    especie: str = "Humano"


    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def get_especie(cls):
        return f"Esta persona es de la especie {cls.especie}" 

    @staticmethod
    def describir_especie():
        return "Somos organismos multicelulares."
persona = Persona("Hugo")
print(persona.get_especie())
print(persona.describir_especie())