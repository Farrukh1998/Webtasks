class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None
    def enqueue(self, element):
        self.size += 1
        if self.head == None:
            self.head = Node(element)
            self.tail = self.head
        else:
            new_node = Node(element)
            self.tail.next = new_node
            self.tail = new_node
    def dequeue(self):
        self.size -= 1
        current = self.head
        self.head = current.next
        current.next = None
        return current.data
    def sizeOfQueue(self):
        return self.size
    def printAll(self):
        cur = self.head
        while(cur):
            print(cur.data, end = ' ')
            cur = cur.next
        print()
    def rec(self):
        if q.sizeOfQueue() == 0:
            return
        item = q.dequeue()
        self.rec()
        q.enqueue(item)
    def recWithoutRecursion(self):
        cur = self.head
        prev = self.head
        cur = cur.next
        prev.next = None
        while cur != None:
            acc = cur.next
            cur.next = prev
            prev = cur
            cur = acc
        self.head = prev


q = QueueLinkedList()
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
print(q.dequeue())
q.printAll()
#rec(q)
#q.printAll()
q.recWithoutRecursion()
q.printAll()
