import random


def lineal_search(lista: list , objetivo :int):
    

    find = [True for elemento in lista if elemento == objetivo]

    return find

if __name__ == '__main__':
    tamañolista = int(input("De que tamaño es la lista: "))
    objetivo = int(input("Que numero quieres encontrar: "))
    
    lista = [random.randint(0,100) for i in range(tamañolista)]
    
    
    print(lista)

    print(f"el elemento {objetivo} {"esta" if lineal_search(lista,objetivo) else "no esta"} en la lista")