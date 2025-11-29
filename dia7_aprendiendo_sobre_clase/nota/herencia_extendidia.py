# Otro ejemplo de herencia multiple
class Padre:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrarNombre(self):
        return f"El padre se llama: {self.nombre}"
    
    def view_padre(self):
        return "El abuelo de ali zorrilla garcia"

class Hijo(Padre):
    def __init__(self, nombre, apellido):
        super().__init__(nombre)
        self.apellido = apellido
    
    def mostrarNombre(self):
        return f"El hijo se llama: {self.nombre} {self.apellido}"
    
    def view_hijo(self):
        return "soy el hijo de hugo"

class Nieto(Hijo):
    def __init__(self, nombre, apellido, apellido_materno):
        super().__init__(nombre, apellido)
        self.apellido_materno = apellido_materno
    
    def mostrarNombre(self):
        return f"El nieto se llama: {self.nombre} {self.apellido} {self.apellido_materno}"
    
    def view_nieto(self):
        return "soy el hijo de rafael zorrilla"

padre = Padre("Hugo")
hijo = Hijo("Rafael", "Zorrilla")
nieto = Nieto("Ali", "Zorrilla", "Garcia")
print(padre.mostrarNombre())
print(hijo.view_padre())
print(nieto.view_hijo())
