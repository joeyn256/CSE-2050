from LinkedListTest import Node,LinkedList

class LinkedQueue:
    def __init__(self):
        self._L = LinkedList()

    def enqueue(self,item):
        self._L.addlast(item)

    def dequeue(self):
        return self._L.removefirst()

    def peek(self):
        item = self.removefirst()
        self._L.addfirst(item)
        return item

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0