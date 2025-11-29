from random import choice


def lanzar_moneda():
    return choice(["Cara", "Cruz"])


def probar_suerte(resultado, lista_numeros):
    if resultado == "Cara":
        print("La lista se autodestruirá")
        lista_numeros.clear()
        return lista_numeros
    elif resultado == "Cruz":
        print("La lista fue salvada")
        return lista_numeros


lista_numeros = [1, 2, 17, 7, 2, 7]
resultado = lanzar_moneda()
probar_suerte(resultado, lista_numeros)
