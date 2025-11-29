# Cuenta Bancaria
from os import system

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # Metodos
    def __str__(self):        
        print(f"Cliente: {self.nombre} {self.apellido}")
        print(f"Cuenta: {self.numero_cuenta}")
        print(f"Balance: {self.balance}")
    
    def depositar(self, cantidad):
        self.balance += cantidad
    
    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes")
        else:
            self.balance -= cantidad
    
    def mostrar_balance(self):
        print(f"Balance: {self.balance}")
    

def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    balance = float(input("Ingrese su balance: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)

def anuncio(mensaje):
    palabra = f"""
    {"#" * (len(mensaje) + 4)}
    # {mensaje} #
    {"#" * (len(mensaje) + 4)}
    """
    print(palabra)

def menu():
    anuncio("Cuenta Bancaria")
    print("1. Crear cliente")
    print("2. Mostrar cliente")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Salir")
    opcion = int(input("Ingrese su opcion: "))
    return opcion

def main():    
    while True: 
        opcion = menu()
        match opcion:
            case 1:
                system("clear")
                anuncio("Crear cliente")
                cliente = crear_cliente()
                input("Presione una tecla para continuar...")
            case 2:
                system("clear")
                anuncio("Mostrar cliente")
                cliente.__str__()
                input("Presione una tecla para continuar...")
            case 3:
                system("clear")
                anuncio(f"Depositar dinero en la cuenta de {cliente.nombre} {cliente.apellido}, saldo actual: {cliente.balance}")   
                cliente.depositar(float(input("Ingrese la cantidad a depositar: ")))
                print(f"Saldo actual: {cliente.balance}")
                input("Presione una tecla para continuar...")
            case 4:
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
