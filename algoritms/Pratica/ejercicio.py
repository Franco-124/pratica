"""
Su tarea es hacer 
una función que pueda tomar cualquier número 
entero no negativo como argumento y devolverlo 
con sus dígitos en orden descendente. 
Esencialmente, reorganice los dígitos para crear 
el número más alto posible.
"""
def func(numero: int) -> int:
    numero = str(numero)
    result = numero[::-1]
    result = int(result)
    return result

print(func(123456789)) # 987654321



  