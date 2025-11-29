def crear_estructura():
    # Definir estructura
    estructura = {
        "proyecto": {
            "src": ["main.py", "utils.py"],
            "data": ["input.csv", "output.json"],
            "docs": ["README.md"],
        }
    }

    base = Path("mi_proyecto")

    for carpeta, archivos in estructura["proyecto"].items():
        # Crear carpeta
        (base / carpeta).mkdir(parents=True, exist_ok=True)

        # Crear archivos en la carpeta
        for archivo in archivos:
            (base / carpeta / archivo).touch()

    print("Estructura creada!")


crear_estructura()
