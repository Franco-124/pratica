#Queues basadas en Nodes


class DoubleNode:

    def __init__(self, data=None
                  ,next= None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def enqueue(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1
    
    def dequeue(self):
        aux = self.head
        if self.count == 1:
            self.head = None
            self.count-=1
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
        return aux.data


def main():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue.dequeue())
    print(queue.dequeue())
    print("--------")
    print(queue.head.data)
   
    
    print("size------")
    print(queue.count)
main()

   