from typing import Union



def unique_in_order(sequence: Union[str, int]):
    result = []
    for x in sequence:
        if not result or x !=result[-1]:
            result.append(x)
    return result

print(unique_in_order('AAAABBBCCDAABBB')) # ['A', 'B', 'C', 'D', 'A', 'B']



def aprove_pin(pin :str):


    approved= [True if len(pin) == 4 or len(pin) == 6 else False]

    return approved

result = aprove_pin("1234")
print(result)



