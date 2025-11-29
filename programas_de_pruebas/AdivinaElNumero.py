palabra = "Python"
lista = []
for indice, letra in enumerate(palabra):
    tuple = tuple(indice, letra)
    lista.append(tuple)

print(lista)
