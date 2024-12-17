class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None
    

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.pre = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node
            new_node.pre = current
            new_node.next = None

    def prepend(self ,data):
        if self.head is None:
            new_node = Node(data)
            new_node.pre = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.pre = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.pre = None

    

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    


dllist = DoubleLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)


dllist.prepend(5)
dllist.print_list() # 1 2 3 4