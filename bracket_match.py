#!/usr/bin/env python
# -*- coding: utf-8 -*-
#栈在括号匹配中的应用
#http://www.cnblogs.com/linxiyue/p/3556875.html
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
def match(i,j):
    print i,j
    opens="({["
    closes=")}]"
    print opens.index(i)
    return  opens.index(i)==closes.index(j)

def synstaxChecker(string):
    balance=True
    s=Stack()
    for x in string:
        if x in "({[":
            s.push(x)
        elif x in ")}]":
            if s.isEmpty():
                balance=False
                break
            else:
                i=s.pop()
                if not match(i,x):
                    balance=False
                    break

    if not s.isEmpty():
        balance=False
    return balance
print synstaxChecker("{[[]}")
