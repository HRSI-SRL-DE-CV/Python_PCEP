user = "Manuel"
password = "Patito123"




user_input = input("Ingrese su usuario ")
password_input = input("Ingrese su password ")

if user == user_input:
    if password == password_input:
        print("Bienvenido Manuel")
    else:
        print("Su password es incorrecto")
elif user_input == "Marco":
    print("Marco no necesita password")
elif user_input == "Pedro":
    print("Pedro es tambien un administrador")
else:
    print("Su usuario es erroneo")

