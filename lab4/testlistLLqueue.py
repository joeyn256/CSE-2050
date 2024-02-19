from LinkedList import Node, LinkedList
from ADT import Queue_LL, TestListQueue
import unittest

class TestQueue(unittest.TestCase, TestListQueue):
    Queue = Queue_LL
if __name__ == '__main__':
    unittest.main()