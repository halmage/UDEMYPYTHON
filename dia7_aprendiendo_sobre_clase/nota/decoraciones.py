def login(func):
    def wrapper():
        user_t = "hugo"
        password_t = "123"
        print("Ingrese su usuario: ")
        user = input()
        print("Ingrese su contraseña: ")
        password = input()
        if user == user_t and password == password_t:
            print("Login exitoso")
            return func()
        else:
            print("Login fallido")
    return wrapper

@login
def mostrarDatos():
    print("Vamos amigo puedes pasar")