# ejemplo de acoplamiento fuerte
class Mascota:
     tiene_patas = True
     pass

class Perro():
    def correr(self, velocidad):
        if Mascota.tiene_patas:
            self.velocidad = velocidad
            
mi_mascota = Perro()
mi_mascota.correr("rápido")
print(mi_mascota.velocidad)