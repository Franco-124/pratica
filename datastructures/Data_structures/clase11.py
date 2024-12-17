# Linked list

from clase10 import Node


class SinglyLinkedList:

    def __init__(self):
        self.first = None
        self.size  = 0

    
    def append(self, data):
        node = Node(data)


        if self.first == None:
            self.first = node
        
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = node
        
        self.size += 1
    

    def size(self):
        return str(self.size)
    
    def iter(self):
        aux = self.first
        while aux:
            val = aux.data
            aux = aux.next
            yield val
    
    def delete(self, data):
        aux = self.first
        prev = self.first
        
        while aux:
            if aux.data == data:
                if aux == self.first:
                    self.first = aux.next
                else:
                    prev.next = aux.next
                self.size -= 1
                return True
            prev = aux
            aux = aux.next
    
    def search(self, data): 

        for node in self.first:
            if data == node:
                print("Found")
            else:
                print("Not found")
    
    def clear(self):
        self.first = None
        self.head = None
        self.size = 0
    

def main():
    words = SinglyLinkedList()
    """ words.append('egg')
    words.append('ham')
    words.append('spam')
    
    current = words.first

    while current:
        print(current.data)
        current = current.next
    

    for word in words.iter():
        print(word)
    """

    head = None
    for count in range(1, 5):
        head = Node(count, head)
    
    while head != None:
        print(head.data)
        head = head.next

main()
    
