#!/usr/bin/env python
# -*- coding: utf-8 -*-
#十进制转化成二进制
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
def demical_to_bin(dec):
    s=Stack()
    cur=dec
    while cur>0:
        a=cur%2
        cur=cur/2
        s.push(a)
    binstr=''
    while not s.isEmpty():
        binstr+=str(s.pop())
    return binstr
print demical_to_bin(5)
print demical_to_bin(100)
