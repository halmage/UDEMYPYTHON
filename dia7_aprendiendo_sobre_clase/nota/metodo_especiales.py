class Musica:
    # __init__ es el constructor
    def __init__(self, nombre, genero, canciones):
        self.nombre = nombre
        self.genero = genero
        self.canciones = canciones
    
    #__str__ es el metodo que se ejecuta cuando se usa la funcion print
    def __str__(self):
        return f"{self.nombre} - {self.genero}"
    
    #__len__ es el metodo que se ejecuta cuando se usa la funcion len()
    def __len__(self):
        return self.canciones
    
    #__del__ es el metodo que se ejecuta cuando se usa la funcion del()
    def __del__(self):
        print(f"Se ha eliminado la lista de reproduccion {self.nombre}")

musica = Musica("Hugazo", "Pop", 36)
print(musica)
print(str(musica))
print(len(musica))
del(musica)