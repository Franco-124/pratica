import random

class Array ():
    def __init__(self, capacity , fill_value = None):
        self.items = []
        for i in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter_(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index , new_item):
        self.items[index] = new_item

    def __contains__(self, item):
        return item in self.items
    
    def __Add__(self):
        return random.randint(1,100)
    
    def __sum__(self):
        result = 0
        for i in self.items:
            result += i
        return result
    
    def __sub__(self):
        result = 0
        for i in self.items:
            result -= i
        return result
       



def main():
    menu = Array(5)

    for i in range(5):
        menu[i] = menu.__Add__()

    print(menu)

    print(menu.__sum__())
  
    

main()


