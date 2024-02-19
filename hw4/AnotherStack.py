from StackADT import ADT

class AnotherStack(ADT):
    def pop(self):
        try:
            return self._L.pop()
        except IndexError:
            raise RuntimeError("pop from empty stack")

if __name__ == '__main__':
    s = AnotherStack()
    s.push(5)
    s.pop()
    s.pop()