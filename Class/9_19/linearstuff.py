from LinearADTs import Stack_Wrapper, Queue_Wrapper, Deque_Wrapper
import unittest

class TestStackWrapper(unittest.TestCase):
    def test_init(self):
        S = Stack_Wrapper()
        self.assertEqual(len(S), 0)

    def test_pop(self):
        S = Stack_Wrapper()
        n = 10
        for i in range(n):
            S.push(i)

        for i in range(n):
            self.assertEqual(S.pop(), n-1-i)
unittest.main() # runs all unittests above
