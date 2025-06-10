"""Ejercicio 3: Calcular la suma de los dígitos de un número elevado a una potencia
Planteamiento: Crea una función que reciba dos parámetros: un número entero positivo y un exponente. La función debe calcular el número elevado al exponente dado, luego sumar todos los dígitos del resultado y devolver esa suma. Por ejemplo, si el número es 2 y el exponente es 3, calcula  2^3 = 8, y la suma de los dígitos es 8. Si el número es 5 y el exponente es 2, calcula 5^2 = 25, y la suma de los dígitos es 2 + 5 = 7."""

def suma_digitos_potencia():
    base = int(input("Ingrese un número entero positivo (base): "))
    exponente = int(input("Ingrese el exponente (entero no negativo): "))
    
    if base < 0 or exponente < 0:
        print("Error: ambos números deben ser enteros no negativos.")
        return
    
    resultado = base ** exponente
    suma_digitos = sum(int(digito) for digito in str(resultado))
    
    print(f"{base}^{exponente} = {resultado}")
    print(f"Suma de los dígitos del resultado: {suma_digitos}")


suma_digitos_potencia()