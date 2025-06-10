"""Ejercicio 2: Convertir un número decimal a binario
Planteamiento: Escribe una función que reciba un número entero positivo y devuelva una cadena con su representación en binario (base 2). Por ejemplo, si se ingresa 10, la función debe devolver "1010". No uses funciones integradas de conversión a binario; implementa la lógica dividiendo el número y construyendo la cadena manualmente."""


def decimal_a_binario():
    num = int(input("Ingrese un número entero positivo para convertir a binario: "))
    if num < 0:
        print("Error: El número debe ser un entero positivo.")
        return
    if num == 0:
        print("La representación binaria de 0 es 0")
        return
    binario = ""
    while num > 0:
        residuo = num % 2
        binario = str(residuo) + binario
        num = num // 2
    print(f"La representación binaria es: {binario}")
    
decimal_a_binario()
