from os import system
import time


def ingresoDePalabra():
    # Esta función solicita al usuario que ingrese una palabra y valida que solo contenga letras.
    palabra = input("Ingrese una palabra: ").lower()
    while not palabra.isalpha():
        print("Error: Solo se permiten letras.")
        palabra = input("Ingrese una palabra: ").lower()
    return palabra


def validandoPalabra(palabra):
    # Esta función valida si la palabra ingresada tiene letras repetidas.
    # Retorna True si hay letras repetidas, False si no las hay.
    return True if len(palabra) != len(set(palabra)) else False


def elimianarLetrasRepetidas(palabra):
    # Esta función elimina las letras repetidas de la palabra ingresada.
    return dict.fromkeys(palabra, 0).keys()


def ordenandoLetras(palabra):
    # Esta función ordena las letras de la palabra ingresada en orden alfabético.
    lista = list(palabra)
    lista.sort()
    return lista


def juntarLetras(palabra):
    # Esta función junta las letras de la palabra en una cadena.lista = list(palabra)
    lista = list(palabra)
    return "".join(palabra)


def main():
    # Esta es la función principal que ejecuta el programa.
    while True:
        #
        # palabra: Variable que almacena la palabra ingresada por el usuario.
        # v_pablabra: Variable que almacena el resultado de la validación de la palabra.
        # e_letra_rept: Variable que almacena las letras de la palabra sin repeticiones.
        # ord_letras: Variable que almacena las letras ordenadas alfabéticamente.
        # j_letras: Variable que almacena las letras de la palabra sin repeticiones en una cadena.
        #
        palabra = ingresoDePalabra()
        v_palabra = validandoPalabra(palabra)
        e_letra_rept = elimianarLetrasRepetidas(palabra)
        ord_letras = ordenandoLetras(e_letra_rept)
        j_letras = juntarLetras(e_letra_rept)

        # Imprimir resultados según si hay letras repetidas o no.
        if v_palabra:
            system("clear")
            print("--------------------------------")
            print("Palabra ingresada:", palabra)
            print("Hay letras repetidas en la palabra.")
            print("-> Palabra sin letras repetidas:", j_letras)
            print("-> Palabra ordenada alfabéticamente:", "".join(ord_letras))
            print("-> Cantidad de letras diferentes:", len(j_letras))
            print("--------------------------------")
        else:
            print("--------------------------------")
            print("-> Palabra ingresada:", palabra)
            print("-> No hay letras repetidas en la palabra.")
            print("--------------------------------")

        # Preguntar al usuario si desea continuar
        continuar = input("¿Desea ingresar otra palabra? (s/n): ").lower()
        while continuar not in ("s", "n"):
            print(
                "Error: Respuesta no válida. Ingrese 's' para continuar o 'n' para salir."
            )
            continuar = input("¿Desea ingresar otra palabra? (s/n): ").lower()

        if continuar == "s":
            system("clear")
            print("continuando...")
            time.sleep(1)
            system("clear")
            continue
        else:
            system("clear")
            print("Saliendo del programa...")
            time.sleep(1)
            system("clear")
            break


if __name__ == "__main__":
    main()
