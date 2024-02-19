import unittest
from LinkedList import Node,LinkedList
class TestListQueue(unittest.TestCase):
    def testinit(self):
        q = ListQueue()
    def testaddandremoveoneitem(self):
        q = ListQueue()
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 3)
    def testalternatingaddremove(self):
        q = ListQueue()
        for i in range(1000):
        q.enqueue(i)
        self.assertEqual(q.dequeue(), i)
    def testmanyoperations(self):
        q = ListQueue()
    for i in range(1000):
    q.enqueue(2 * i + 3)
    for i in range(1000):
        self.assertEqual(q.dequeue(), 2 * i + 3)
    def testlength(self):
        q = ListQueue()
        self.assertEqual(len(q), 0)
    for i in range(10):
        q.enqueue(i)
        self.assertEqual(len(q), 10)
    for i in range(10):
        q.enqueue(i)
        self.assertEqual(len(q), 20)
    for i in range(15):
        q.dequeue()
        self.assertEqual(len(q), 5)
    
if __name__ == '__main__':
    unittest.main()