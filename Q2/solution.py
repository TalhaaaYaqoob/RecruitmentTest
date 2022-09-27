class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def deleteNode(self, n):
        first = self.head
        second = self.head
        for i in range(n):
            if second.next ==None:
                if i ==n -1:
                    self.head = self.head.next
                return self.head
            second = second.next
        while second.next != None:
            second = second.next
            first = first.next
        first.next = first.next.next
    def printList(self):
        tmp_head = self.head
        while tmp_head != None:
            print(tmp_head.data, end=" ")
            tmp_head = tmp_head.next
            

lists = Linkedlist()
lists.push(5)
lists.push(4)
lists.push(3)
lists.push(2)
lists.push(1)

lists.printList()
lists.deleteNode(2)
print()
lists.printList()
