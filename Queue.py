#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python 队列实现
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def isEmpty(self):
        return self.queue==[]
    def dequeue(self):
        if not self.isEmpty():
            a=self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError,"queue is empty"
    def size(self):
        return len(self.queue)
q=Queue()
print  q.isEmpty()
q.enqueue(1)
q.enqueue(3)
print q.dequeue()
print q.size()