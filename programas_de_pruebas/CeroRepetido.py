# Importando librerías necesarias
from os import system


class CeroRepetido:
    def __init__(self):
        self.contador = 0
        self.cant_cero_consecutivos = 0
        self.bandera = False
        self.lista = []

    def entryData(self):
        # Solicitar un número al usuario y validar que sea un entero positivo
        numero = input("Introduce un número: ")
        while not numero.isdigit() or numero < "0":
            print("Por favor, introduce un número válido.")
            numero = input("Introduce un número: ")
        numero = int(numero)
        return numero

    def evaluarCeroIngresados(self, numero):
        # Evaluar si el número ingresado es cero
        if numero == 0:
            # Si el número es cero, se incrementa el contador
            self.contador += 1
        else:
            # Si no es cero, se reinicia el contador
            self.contador = 0

        # Si el contador llega a 2, se activa la bandera
        if self.contador == 2:
            self.cant_cero_consecutivos += 1
            self.bandera = True

        # Si el contador es mayor que 2 y su division por 2 es igual a 2,
        # se incrementa la cantidad de ceros consecutivos
        if self.contador > 2 and self.contador % 2 == 0:
            self.cant_cero_consecutivos += 1

    def imprimirMensaje(self):
        # Imprimir un mensaje si la bandera está activa
        if self.bandera:
            print("Se han ingresado dos ceros consecutivos.")
            print("--Lista de números ingresados--\n")
            print(self.lista, "\n")
            print("----------------------------\n")
            print(f"cantidad de cero consecutivos: {self.cant_cero_consecutivos}\n")
            print("----------------------------\n")
            print(f"bandera: {self.bandera}")
        else:
            print("Se han ingresado dos ceros consecutivos.")
            print("--Lista de números ingresados--\n")
            print(self.lista, "\n")
            print("----------------------------\n")
            print(f"cantidad de cero consecutivos: {self.cant_cero_consecutivos}\n")
            print("----------------------------\n")
            print(f"bandera: {self.bandera}")

    def main(self):
        # Método principal para ejecutar el programa
        while True:
            # Solicitar un número al usuario
            numero = self.entryData()

            # Evaluar el número ingresado y actualizar la lista
            self.evaluarCeroIngresados(numero)

            # Agregar el número a la lista
            self.lista.append(numero)

            # Imprimir la lista actual
            print("Lista actual:", self.lista)

            # Imprimir el contador de ceros consecutivos
            print("Contador de ceros consecutivos:", self.contador)

            # Imprimir la cantidad de ceros consecutivos
            print("Cantidad de ceros consecutivos:", self.cant_cero_consecutivos)

            # Preguntar al usuario si desea continuar
            print("Quieres continuar? (s/n):")
            respuesta = input().lower()
            if respuesta == "s":
                system("clear")
                continue
            elif respuesta == "n":
                break

        # Imprimir el mensaje basado en la evaluación
        system("clear")
        self.imprimirMensaje()


if __name__ == "__main__":
    # Crear una instancia de la clase y ejecutar el método principal
    cero_repetido = CeroRepetido()
    cero_repetido.main()
