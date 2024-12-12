#First way
from collections import Counter
def func(caraters):
    contador = {}
    for c in caraters:
        if c in contador:
            contador[c]+=1
        else:
            contador[c]=1
    return contador


result = func("22Aaab,2,")
print(result)
print('*'*5)

def func2(palabra):
    contador = Counter(palabra)
    return contador

result2 = func("prlccc.,w222")

print(result2)


def accum(s):
    return '-'.join((char * (i + 1)).capitalize() for i, char in enumerate(s))

# Test cases
print(accum("abcd"))     # "A-Bb-Ccc-Dddd"
print(accum("RqaEzty"))  # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt"))     # "C-Ww-Aaa-Tttt"