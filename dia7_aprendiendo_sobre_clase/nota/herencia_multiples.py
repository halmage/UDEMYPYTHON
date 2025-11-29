<- Herencia multiple (herencia de varias clases) ->
# Ejemplo de herencia multiple
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Volador():
    def volar(self):
        return f"{self.nombre} está volando"

class Nadador():
    def nadar(self):
        return f"{self.nombre} está nadando"

class Avestruz(Animal, Volador):
    def __init__(self, nombre):
        super().__init__(nombre)

class Pato(Animal, Volador, Nadador):
    def __init__(self, nombre):
        super().__init__(nombre)

avestruz = Avestruz("Avestruz")
pato = Pato("Pato")
print(avestruz.volar())
print(pato.volar())
print(pato.nadar())
print(pato.nombre)