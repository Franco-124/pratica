#Ordenamiento burbuja


def bubble_sort(lista):
    for i in range (len(lista)):
        for j in range(0 ,len(lista) - i -1):#O(n) *O(n) = O(n*n) = O(n^2) 
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
     
            
    return lista


print(bubble_sort([8,6,9,10,5,6,7]))