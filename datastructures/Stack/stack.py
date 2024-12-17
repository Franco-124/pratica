from Node import Node


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0
    

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
    
        self.size += 1
    
    
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return "The stack is empty"
    
    def pop_element(self, data):
        aux = self.top
        prev = None
        while aux:
            if aux.data == data:
                if prev:
                    prev.next = aux.next
                else:
                    self.top = aux.next
                self.size -= 1
                return
            prev = aux
            aux = aux.next

      
    

    def search(self, data):
        aux = self.top
        while aux:
            if aux.data == data:
                return True
            aux = aux.next
        return False
    
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"
    

    def clear(self):
        while self.top:
            self.pop()
    

    def cont_elements(self):
        return self.size
    

    def print_stack(self):
        aux = self.top
        while aux:
            print(aux.data)
            aux = aux.next
        print('-----------------')


def main():
    stack = Stack()
    stack.push('egg')
    stack.push('ham')
    stack.push('spam')
    
    print(stack.peek())

    search = stack.search('egg')
    if search:
        print("The element is in the stack")
    else:
        print("The element is not in the stack")
    
    print(stack.cont_elements())

    stack.pop_element('ham')

    stack.print_stack()



main()
    