# Ejercicio 7
# Autor: Alex

# Escribe un programa que solicite al usuario una temperatura en 
# escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. 
# La fórmula de conversión que se usa para este cálculo es: Celsius = (5/9) * (Fahrenheit-32). 
# Mostrar el resultado utilizando dos decimales.

Fahrenheit = float(input("Introduce la temperatura de Fahrenheit (F): "))

Celsius = (5/9) * (Fahrenheit-32)

print(f"La temperatura de Celsius es {Celsius:.2f} ºC.")