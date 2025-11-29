# Ejemplo de herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre        
    
def sonido(self):
    pass

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"       
    
perro = Perro("Perro")
gato = Gato("Gato")
print(perro.sonido())
print(gato.sonido())