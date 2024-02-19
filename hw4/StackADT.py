class ADT:
    def __init__(self):
        self._L = []

    def push(self, item):
        self._L.append(item)
    
    def pop(self):
        return self._L.pop()

    def peek(self):
        return self._L[-1]

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0

if __name__ == '__main__':
    Stack1 = ADT()
    assert Stack1.isempty()
    
    Stack1.push(1)
    Stack1.push('hello')
    Stack1.push(13)
    
    assert Stack1.peek() == 13
    assert len(Stack1) == 3
    
    Stack1.pop()
    assert Stack1.peek() == 'hello'
    assert len(Stack1) == 2
    assert not Stack1.isempty()



    

