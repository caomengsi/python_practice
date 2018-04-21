class Stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return  self.stack==[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            raise IndexError,'pop from empty stack'
        return  self.stack.pop()
    def size(self):
        return len(self.stack)
m=Stack()
print m.isEmpty()
m.push(1)
m.push(2)
print m
print m.size()
print m.pop()
m.pop()
# m.pop()