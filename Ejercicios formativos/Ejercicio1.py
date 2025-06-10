"""Ejercicio 1: Calcular el factorial de un número
Planteamiento: Crea una función que reciba un número entero no negativo como parámetro y devuelva su factorial. El factorial de un número n es el producto de todos los enteros positivos desde 1 hasta n (por ejemplo, 5! = 5 * 4 * 3 2   1 = 120). Asegúrate de manejar el caso especial donde n = 0, que devuelve 1."""

def factorial():
    n = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
    if n < 0:
        print("Error: El número debe ser un entero no negativo.")
        return
    if n == 0:
        print("El factorial de 0 es 1")
        return
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    print(f"El factorial de {n} es {resultado}")
    
factorial()
