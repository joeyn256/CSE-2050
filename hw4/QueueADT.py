class QueueADT:
    def __init__(self):
        self._head = 0
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def peek(self):
        return self._L[self._head]

    def dequeue(self):
        item = self._L[self._head]
        self._head += 1
        if self._head > len(self._L)//2:
            self._L = self._L[self._head:]
            self._head = 0
        return item

    def __len__(self):
        return len(self._L) - self._head

    def isempty(self):
        return len(self) == 0

if __name__ == '__main__':
    L1 = QueueADT()
    assert L1.isempty()
    L1.enqueue(3)
    L1.enqueue('hello')
    L1.enqueue(13)
    # 3 --> 'hello' --> 13
    assert L1.peek() == 3
    L1.dequeue()
    # 'hello' --> 13
    assert L1.peek() == 'hello'
    assert len(L1) == 2
    assert not L1.isempty()