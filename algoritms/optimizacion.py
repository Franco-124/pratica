

def morral(size , pesos ,values ,n ):
    
    if  n == 0 or size == 0:
        return 0
    
    if pesos [n - 1 ] > size:
        return morral(size , pesos, values, n -1)
    
    return max(values[n - 1] + morral(size - pesos[n - 1] , pesos, values , n - 1),
               morral(size, pesos , values , n - 1))




if __name__ == "__main__":
    values = [60, 100, 120]
    pesos = [10, 20, 30]
    size = 50
    n = len(values)
    print(morral(size, pesos, values, n))  # 220