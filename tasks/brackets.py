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

lol = input()
mx = 0
s = Stack()
ln = 0
for i in lol:
    if i == '(':
        s.push(i)
    else:
        if s.sizeOfStack() != 0:
            s.pop()
            ln += 2
        else:
            mx = max(ln, mx)
            ln = 0
mx = max(ln, mx)
print(mx)
