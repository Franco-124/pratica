
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None



for count in range(1, 5):
    head = None
    head = Node(count, head)
while head !=None:
    print(head.data)
    head = head.next