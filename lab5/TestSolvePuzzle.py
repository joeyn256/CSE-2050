from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
    def testClockwise(self):
    #Tests a board solveable using only CW moves
        test1 = puzzle([0])
        self.assertTrue(test1)
        test2 = puzzle([2,1,1,0])
        self.assertTrue(test2)
    def testCounterClockwise(self):
    #Tests a board solveable using only CCW moves
        test1 = puzzle([14,9,11,0])
        self.assertTrue(test1)
        test2 = puzzle([7,2,0])
        self.assertTrue(test2)
    def testMixed(self):
    #Tests a board solveable using only a combination of CW and CCW moves
        test1 = puzzle([3,1,2,0])
        self.assertTrue(test1)
        test1 = puzzle([7,2,0])
        self.assertTrue(test1)
        self.assertTrue([3,6,4,1,3,4,2,0])

    def testUnsolveable(self):
    #Tests an unsolveable board
        test1 = puzzle([2,0,2,0])
        test2 = puzzle([6,0,6,0])
        test3 = puzzle([4,0])
        self.assertFalse(test1)
        self.assertFalse(test2)
        self.assertFalse(test3)
        self.assertFalse([3,4,1,2,0])

unittest.main()
