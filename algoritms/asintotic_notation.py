#crecimiento lineal
def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)
#crecimiento cuadratico
def f(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#crecimiento exponencial
def fibonacci(n):
    if n == 0 or n ==1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


