# Ejercicio 9
# Autor: Alex

# Escribe un programa que solicite un texto y que escriba el texto en mayúsculas, 
# en minúsculas,  con la primera letra en mayúscula, 
# y con la primera letra de cada palabra en mayúscula.

texto = input("Introduce un texto: ")

# Convertir el texto a mayúsculas
mayusculas = texto.upper()
# Convertir el texto a minúsculas
minusculas = texto.lower()
# Convertir solo la primera letra del texto a mayúscula
primera_mayuscula = texto.capitalize()
# Convertir la primera letra de cada palabra a mayúscula
titulo = texto.title()

print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)
print("Primera letra en mayúscula:", primera_mayuscula)
print("Primera letra de cada palabra en mayúscula:", titulo)
