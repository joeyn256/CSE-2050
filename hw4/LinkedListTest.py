from dataclasses import dataclass


class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedListStack:
    def __init__(self):
        self._head = None

    def addfirst(self, item):
        self._head = Node(item, self._head)

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        return item

class LinkedListQueue:
    def __init__(self):
        self._head = None

    def addfirst(self, item):
        self._head = Node(item, self._head)

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        return item

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            currentnode = self._head
            while currentnode.link is not None:
                currentnode = currentnode.link
            currentnode.link = Node(item)
    def removelast(self):
        if self._head.link is None:
            return self.removefirst()
        else:
            currentnode = self._head
            while currentnode.link.link is not None:
                currentnode = currentnode.link
            item = currentnode.link.data
            currentnode.link = None
            return item

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def addfirst(self, item):
        self._head = Node(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._len += 1

    def removefirst(self):
        currentnode = self._head.link
        self._head = currentnode
        self._len -= 1
        return currentnode

    def addlast(self, item):
        if self._tail is None:
            self.addfirst(item)
        else:
            self._tail.link = Node(item)
            self._tail = self._tail.link
            self._len += 1

    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            currentnode = self._head 
            while currentnode.link is not self._tail:
                currentnode = currentnode.link
            item = self._tail.data
            self._tail = currentnode
            self._tail.link = None
            self._len -= 1
            return item

    def __len__(self):
        return self._len


if __name__ == '__main__':
    n3 = Node('hello')
    n2 = Node(1, n3)
    n1 = Node('cheese', n2)

    assert n2.data == 1
    a1 = LinkedListQueue()


    






