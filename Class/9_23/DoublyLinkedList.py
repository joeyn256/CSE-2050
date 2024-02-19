class Node:
    def __init__(self, _item, _next=None, _prev=None):
        self._item = _item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        p = self._prev._item if self._prev else None
        n = self._next._item if self._next else None
        return f"Node({self._item}, prv={p}, next={n})"



class DoublyLinked List:




from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

class TestDLL(unittest.TestCase):
    def test_init(self):
        dll = DLL()

n1 = Node('a')
n2 = Node('b')
n3 = Node('c')

n1._next = n2

n2._prev = n1
n2._prev = 