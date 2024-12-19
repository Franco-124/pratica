#Crear una Queue basado en dos stacks


class Queue:

    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
    
    def enqueue(self , data):
        self.inbound_stack.append(data)
    
    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop() 
    
def main():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue.dequeue())
    print(queue.outbound_stack)

main()