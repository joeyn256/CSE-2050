class Stack_Wrapper:
#implements Stack ADT w/ List Wrapper
    def __init__(self):
        self._L = [] # composition: a stock *has a* list


    def push(self,item):
        self._L.insert(0, item)
    def pop(self):
        return self._L.pop(0)
    def __len__(self):
        return len(self._L)

class Queue_Wrapper:
    """Implements Queue ADT w/ List Wrapper"""

class Deque_Wrapper:
    """implements Deque ADT w/ List Wrapper"""