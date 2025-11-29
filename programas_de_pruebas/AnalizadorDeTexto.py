poema = "Amor, ese sentimiento que invade mi ser, que me hace soñar despierta y suspirar sin querer."
letra1 = input("Ingrese primera letra: ").lower()
letra2 = input("Ingrese segunda letra: ").lower()
letra3 = input("Ingrese tercera letra: ").lower()

poema_minuscula = poema.lower()

total_letra1 = poema_minuscula.count(letra1)
total_letra2 = poema_minuscula.count(letra2)
total_letra3 = poema_minuscula.count(letra3)

anuncio_cantidad_letras = """
*******************
|LETRAS INGRESADAS|
*******************
"""
print(anuncio_cantidad_letras)
print(f"Primera letra: {letra1}")
print(f"Segundaa letra: {letra2}")
print(f"Tercera letra: {letra3}")


anuncio_cantidad_letras = """
**********************
|CANTIDADES DE LETRAS|
**********************
"""
print(anuncio_cantidad_letras)
print(f"Cantidad de {letra1}: ", total_letra1)
print(f"Cantidad de {letra2}: ", total_letra2)
print(f"Cantidad de {letra3}: ", total_letra3)

anuncio_cantidad_palabras = """
************************
|CANTIDADED DE PALABRAS|
************************
"""
print(anuncio_cantidad_palabras)
print(f"Cantidad de palabras: ", len(poema.split()))

anuncio_primera_y_ultima_palabras = """
**************************
|PRIMERA Y ULTIMA PALABRA|
**************************
"""
print(anuncio_primera_y_ultima_palabras)
primera_palabra = poema_minuscula.split()[0]
ultima_palabra = poema_minuscula.split()[-1]
print(f"Primera palabra: {primera_palabra}")
print(f"Ultima palabra: {ultima_palabra}")

invertir_palabras = """
*******************
|INVERTIR PALABRAS|
*******************
"""
print(invertir_palabras)
poema_invertido = " ".join(poema_minuscula.split()[::-1])
print(poema_invertido)

buscar_palabra = """
***************
|BUSCAR PALABRA|
***************
"""
print(buscar_palabra)
palabra_buscar = input("Ingrese palabra a buscar: ")
if palabra_buscar in poema_minuscula:
    print(f"{palabra_buscar} está en el poema.")
else:
    print(f"{palabra_buscar} no está en el poema.")
