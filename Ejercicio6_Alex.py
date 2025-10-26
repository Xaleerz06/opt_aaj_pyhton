# Ejercicio 6
# Autor: Alex

# Escribe un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por en 
# coche y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar 
# el consumo del vehículo por cada 100 kilómetros recorridos.


kilometros = float(input("Ingrese la cantidad de kilómetros recorridos: "))
litros = float(input("Ingrese la cantidad de litros de combustible consumidos: "))

consumo = (litros / kilometros) * 100

print(f"El consumo del vehículo es de {consumo:.2f} litros cada 100 km.")