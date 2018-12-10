class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueList:
    def __init__(self):
        self.arr = []
        self.size = 0
    def enqueue(self, element):
        self.size += 1
        self.arr.append(element)
    def dequeue(self):
        self.size -= 1
        return self.arr.pop(0)
    def sizeOfQueue(self):
        return self.size

class QueueLinkedList:
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

class Stack:
    def __init__(self):
        self.arr = []
        self.size = 0
    def push(self, element):
        self.arr.append(element)
        self.size += 1
    def pop(self):
        el = self.arr[self.size - 1]
        self.arr.pop()
        self.size -= 1
        return el
    def top(self):
        return self.arr[self.size - 1]
    def sizeOfStack(self):
        return self.size

class QueueUsingStack():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def enqueue(self, data):
        while (self.stack1.sizeOfStack() > 0):
            self.stack2.push(self.stack1.pop())
        self.stack1.push(data)
        while (self.stack2.sizeOfStack() > 0):
            self.stack1.push(self.stack2.pop())
    def dequeue(self):
        return self.stack1.pop()
    def sizeOfQueue(self):
        return self.stack1.sizeOfStack()

class StackUsingQueue:
    def __init__(self):
        self.queue1 = QueueList()
        self.queue2 = QueueList()
    def push(self, element):
        while self.queue1.sizeOfQueue() > 0:
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1.enqueue(element)
        while self.queue2.sizeOfQueue() > 0:
            self.queue1.enqueue(self.queue2.dequeue())
    def pop(self):
        return self.queue1.dequeue()
    def top(self):
        data = self.queue1.dequeue()
        self.queue2.enqueue(data)
        while self.queue1.sizeOfQueue() > 0:
            self.queue2.enqueue(self.queue1.dequeue())
        while self.queue2.sizeOfQueue() > 0:
            self.queue1.enqueue(self.queue2.dequeue())
        return data
    def sizeOfStack(self):
        return self.queue1.sizeOfQueue()

s = StackUsingQueue()
s.push(1)
s.push(2)
s.push(3)
print(s.top(), s.pop(), s.pop(), s.pop())
q = QueueLinkedList()
q.enqueue(1)
print(q.dequeue())
