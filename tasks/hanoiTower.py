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
    def printAllElements(self):
        while (self.sizeOfStack() > 0):
            print(self.pop(), end = ' ')

class TowerOfHanoi:
    def __init__(self, numDisks):
         self.numDisks = numDisks
         self.towers = [Stack(), Stack(), Stack()]
         for i in range(self.numDisks, -1, -1):
             self.towers[0].push(i)

    def moveDisk(self, fromPole, toPole):
        self.towers[toPole - 1].push(self.towers[fromPole - 1].pop())
        print("moving disk from", fromPole, "to", toPole)
 
    def moveTower(self, height, fromPole, withPole, toPole):
        if height >= 1:
            self.moveTower(height - 1, fromPole, toPole, withPole)
            self.moveDisk(fromPole,toPole)
            self.moveTower(height - 1, withPole, fromPole, toPole)

    def printAll(self):
        for i in range(3):
            self.towers[i].printAllElements()
            print("")

t = TowerOfHanoi(3)
t.moveTower(3, 1, 2, 3)
t.printAll()
