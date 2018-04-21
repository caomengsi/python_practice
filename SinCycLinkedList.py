#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python实现循环单链表
class Node:
    def __init__(self,initdata):
        self.__data=initdata
        self.__next=None
    def getData(self):
        return self.__data
    def getNext(self):
        return self.__next
    def setData(self,newData):
        self.__data=newData
    def setNext(self,newNext):
        self.__next=newNext
class SinCycLinkedList:
    def __init__(self):
        self.head=Node(None)
        self.head.setNext(self.head)
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)
    def search(self,item):
        cur=self.head.getNext()
        while cur !=self.head:
            if cur.getData()==item:
                return True
            cur=cur.getNext()
        return False
    def remove(self,item):
       pre=self.head
       while pre.getNext()!=self.head:
           cur = pre.getNext()
           if cur.getData() == item:
               pre.setNext(cur.getNext())
           pre= pre.getNext()

    def empty(self):
        return self.head.getNext()==self.head
    def size(self):
        count=0
        cur=self.head.getNext()
        while cur != self.head:
            count+=1
            cur=cur.getNext()
        return count
if __name__=='__main__':
    s=SinCycLinkedList()
    print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))
    s.add(6)
    s.add(89)
    print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))

    print s.search(6)
    s.remove(6)
    print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))
