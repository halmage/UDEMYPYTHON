import time
from os import system


def ingresoDeNumeros():
    # Solicita al usuario ingresar tres números enteros y los devuelve en un diccionario.
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))
    return {"a": a, "b": b, "c": c}


def devolverDistintos(**args):
    # Calcula la suma de los tres números y devuelve el mayor, menor o el del medio según las reglas especificadas.
    suma = args["a"] + args["b"] + args["c"]
    lista = [args["a"], args["b"], args["c"]]

    # Si la suma es mayor a 15, devuelve el mayor de los tres números.
    if suma > 15:
        return max(args["a"], args["b"], args["c"])

    # Si la suma es menor a 10, devuelve el menor de los tres números.
    elif suma < 10:
        return min(args["a"], args["b"], args["c"])

    # Si la suma está entre 10 y 15, devuelve el número del medio.
    else:
        lista.sort()
        return lista[1]


def main():
    while True:
        args = ingresoDeNumeros()
        resultado = devolverDistintos(**args)
        print(f"El resultado es: {resultado}")

        # Validación de la respuesta del usuario.
        respuesta = input("¿Desea continuar? (s/n): ")
        while respuesta.lower() not in ["s", "n"]:
            respuesta = input("Respuesta inválida. ¿Desea continuar? (s/n): ")
        if respuesta.lower() == "s":
            system("clear")
            print("Continuando...")
            time.sleep(1)
            system("clear")
        else:
            system("clear")
            print("Saliendo del programa.")
            time.sleep(1)
            system("clear")
            break


if __name__ == "__main__":
    main()
