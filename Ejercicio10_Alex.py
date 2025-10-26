# Ejercicio 10
# Autor: Alex

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por 
# la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en 
# la variable sin tener en cuenta mayúsculas y minúsculas.

Contrasena = "MisSecreta1234"

Contrasena_Guardada = input("Introduce una contraseña si coincide con la guardada: ")

if Contrasena.lower() == Contrasena_Guardada.lower():
    print("Si coincide, Felicidades!!!")
else:
    print("No coincide, Perdiste!!!")
