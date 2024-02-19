from LinkedList import Node,LinkedList

class Stack_L:
    def __init__(self):
        self._L = list()

    def push(self, item):
        self._L.append(item)
    
    def pop(self):
        return self._L.pop()

class Stack_LL:
    def __init__(self):
        self._LL = LinkedList()
    
    def push(self, item):
        self._LL.add_last(item)

    def pop(self):
        return self._LL.remove_last()

class Queue_L:
    def __init__(self):
        self._head = 0
        self._L = list()

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        item = self._L[self._head]
        self._head += 1
        if self._head > len(self._L)//2:
            self._L = self._L[self._head:]
            self._head = 0
        return item


class Queue_LL:
    def __init__(self):
        self._L = LinkedList()

    def enqueue(self,item):
        self._L.add_last(item)

    def dequeue(self):
        return self._L.remove_first()

class TestListStack():
    def __init__(self, func):
        self.L = func
    def testaddandremoveoneitem(self):
        self.L.push(3)
        assert self.L.pop() == 3
    def testalternatingaddremove(self):
        for i in range(1000):
            self.L.push(i)
            assert self.L.pop() == i
    def testmanyoperations(self):
        for i in range(1000):
            self.L.push(2 * i + 3)
        for i in reversed(range(1000)):
            assert self.L.pop() == (2 * i + 3)

class TestListQueue():
    def __init__(self, func):
        self.L = func
    def testaddandremoveoneitem(self):
        self.L.enqueue(3)
        assert self.L.dequeue() == 3
    def testalternatingaddremove(self):
        for i in range(1000):
            self.L.enqueue(i)
            assert self.L.dequeue() == i
    def testmanyoperations(self):
        for i in range(1000):
            self.L.enqueue(2 * i + 3)
        for i in range(1000):
            assert self.L.dequeue() == (2 * i + 3)


def TestListStacks(q = TestListStack(func = Stack_L())):
    q.testalternatingaddremove()
    q.testaddandremoveoneitem()
    q.testmanyoperations()

#Test Stack_L
TestListStacks()
#Test Stack_LL
TestListStacks(TestListStack(func = Stack_LL()))
#Test Queue_L
TestListStacks(TestListQueue(func = Queue_L()))
#Test Queue_LL
TestListStacks(TestListQueue(func = Queue_LL()))