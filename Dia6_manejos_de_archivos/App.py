from pathlib import Path

folder = Path("/home/halmagedecesilia/Documentos/Practice/UDEMYPYTHON/archive/Recetas")


def buscarArchivo():
    print("Ingrese nombre de la carpeta: ")
    archive = input()

    for elemento in folder.iterdir():
        print(elemento.name)


buscarArchivo()
