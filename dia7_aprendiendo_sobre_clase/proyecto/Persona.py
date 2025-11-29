# Cuenta Bancaria
from os import system

class Persona():
    # Clase padre Persona
    # Atributos: nombre, apellido
    # Metodos: __init__
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    # Clase hija Cliente hereda de Persona
    # Atributos: numero_cuenta, balance
    # Metodos: __init__, __str__, depositar, retirar, mostrar_balance
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # Metodos
    def __str__(self):    
        # Metodo que muestra los datos del cliente    
        print(f"Cliente: {self.nombre} {self.apellido}")
        print(f"Cuenta: {self.numero_cuenta}")
        print(f"Balance: {self.balance}")
    
    def depositar(self, cantidad):
        # Metodo que deposita dinero en la cuenta
        self.balance += cantidad
    
    def retirar(self, cantidad):
        # Metodo que retira dinero de la cuenta
        if cantidad > self.balance:
            # Si el saldo es insuficiente
            print("Fondos insuficientes")
        else:
            # Si el saldo es suficiente
            self.balance -= cantidad    

def crear_cliente():
    # Funcion que crea un cliente
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    balance = float(input("Ingrese su balance: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)

def anuncio(mensaje):
    # Funcion que muestra un anuncio
    palabra = f"""
    {"#" * (len(mensaje) + 4)}
    # {mensaje} #
    {"#" * (len(mensaje) + 4)}
    """
    print(palabra)

def menu():
    # Menu del programa
    anuncio("Cuenta Bancaria")
    print("1. Crear cliente")
    print("2. Mostrar cliente")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Salir")
    opcion = int(input("Ingrese su opcion: "))
    return opcion

def main():    
    # Funcion principal 
    while True: 
        opcion = menu()
        match opcion:
            case 1:
                # Crear cliente
                system("clear")
                anuncio("Crear cliente")
                cliente = crear_cliente()
                input("Presione una tecla para continuar...")
            case 2:
                # Mostrar cliente
                system("clear")
                anuncio("Mostrar cliente")
                cliente.__str__()
                input("Presione una tecla para continuar...")
            case 3:
                # Depositar dinero
                system("clear")
                anuncio(f"Depositar dinero en la cuenta de {cliente.nombre} {cliente.apellido}, saldo actual: {cliente.balance}")   
                cliente.depositar(float(input("Ingrese la cantidad a depositar: ")))
                print(f"Saldo actual: {cliente.balance}")
                input("Presione una tecla para continuar...")
            case 4:
                # Retirar dinero
                system("clear")
                anuncio(f"Retirar dinero de la cuenta de {cliente.nombre} {cliente.apellido}, saldo actual: {cliente.balance}")
                cliente.retirar(float(input("Ingrese la cantidad a retirar: ")))
                print(f"Saldo actual: {cliente.balance}")
                input("Presione una tecla para continuar...")
            case 5:
                break
        system("clear")

if __name__ == "__main__":
    main()
