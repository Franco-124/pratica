

class ListQueue:

    def __init__(self):
        self.items = []
        self.size = 0
    

    def enqueue(self, data):
        self.items.append(data)
        self.size += 1
        return self.items
    

    def dequeue(self, data):
        data = self.items.pop()
        self.size -= 1
        return data
    
    def traverse (self):
        total_items = self.size
        for item in range(total_items):
            print(self.items[item])


def main():
    queue = ListQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.traverse()
    queue.dequeue(1)
    print("*"*10)
    queue.traverse()

main()