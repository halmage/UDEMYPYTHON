import time
from os import system as System

while True:
    # Primera pregunta
    print("¿Cuál es tu nombre?")
    respuesta1 = input("")
    # Segunda pregunta
    print("¿Que te gusta hacer?")
    respuesta2 = input("")
    # Combinación de respuestas
    nombre = f"{respuesta1}{respuesta2}"
    # Nombre de la cerveza
    print(
        f"""
          Si combinamos {respuesta1.upper()} y {respuesta2.upper()} obtenemos como nombre \'{nombre.upper()}\' para tu cerveza.
          """
    )
    # Pregunta si le gusta el nombre
    print("¿Te gusto el nombre? (si/no)")
    respuesta3 = input("")
    # Validación de respuesta
    while respuesta3.lower() not in ["si", "no"]:
        print("Por favor, responde con 'si' o 'no'.")
        respuesta3 = input("")
    # Si le gusta el nombre, lo muestra y termina el programa
    if respuesta3.lower() == "si":
        print(f"\n\n¡Genial! Tu nombre es '{nombre.upper()}'")
        break
    # Si no le gusta el nombre, pregunta si quiere intentarlo de nuevo
    else:
        print("¿Quieres intentarlo de nuevo? (si/no)")
        intento = input("")
        while intento.lower() not in ["si", "no"]:
            print("Por favor, responde con 'si' o 'no'.")
            intento = input("")
        if intento.lower() == "no":
            print("¡Hasta luego!")
            break
        else:
            print("Vamos a intentarlo de nuevo.")
            time.sleep(2)
            System("clear")
