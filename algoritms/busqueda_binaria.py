
"""
divide y conquista
el problema se divide en dos en cada iteracion
cual es el peor caso
"""

import random

def binary_search(lista, comienzo, final, objetivo):
    print(f"Estamos buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}")
    
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    
    elif lista[medio] < objetivo:
        return binary_search(lista ,medio + 1 ,final, objetivo)
    
    else:
        return binary_search(lista, comienzo , medio - 1 , objetivo)



if __name__ == '__main__':
    tamaño_lista = int(input("De que tamaño es la lista: "))
    objetivo = int(input("Que numero quieres encontrar: "))
    
    lista = sorted([random.randint(0,100) for i in range(tamaño_lista)])
    encontrado = binary_search(lista, 0 , len(lista), objetivo)
    
    print(lista)

    print(f"el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista")