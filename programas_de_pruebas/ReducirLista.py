def reducir_lista(lista_numeros):
    maximo = 0
    for i in range(len(lista_numeros)):
        if lista_numeros[i] > maximo:
            maximo = lista_numeros[i]
    lista_numeros.remove(maximo)
    lista_numeros = list(set(lista_numeros))
    return lista_numeros


def promedio(lista_numeros):
    suma = 0
    for i in range(len(lista_numeros)):
        suma += lista_numeros[i]
    promedio = float(suma / len(lista_numeros))
    return promedio


lista_numeros = [1, 2, 17, 7, 2, 7]
lista_numeros = reducir_lista(lista_numeros)
promedio = promedio(lista_numeros)
