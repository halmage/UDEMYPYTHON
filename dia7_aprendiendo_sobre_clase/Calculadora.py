from os import system

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 / self.num2
    
    def menu(self):
        print("Menu de opciones")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    
    def main(self):
        while True:
            opcion = self.menu()
            match opcion:
                case 1:                    
                    print(f"La suma de {self.num1} y {self.num2} es {self.suma()}")                    
                    input("Presione enter para continuar...")
                    system("clear")
                case 2:                    
                    print(f"La resta de {self.num1} y {self.num2} es {self.resta()}")                    
                    input("Presione enter para continuar...")
                    system("clear")
                case 3:                    
                    print(f"La multiplicacion de {self.num1} y {self.num2} es {self.multiplicacion()}")                    
                    input("Presione enter para continuar...")
                    system("clear")
                case 4:                    
                    print(f"La division de {self.num1} y {self.num2} es {self.division()}")                    
                    input("Presione enter para continuar...")
                    system("clear")
                case 5:
                    system("clear")
                    print("Hasta luego")
                    break
                case _:
                    print("Opcion invalida")
                    input("Presione enter para continuar...")
                    system("clear")

calculadora = Calculadora(10, 20)
calculadora.main()