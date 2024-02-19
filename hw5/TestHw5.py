from hw5 import solveable, valid_moves
import unittest

class TestValidMoves(unittest.TestCase):
        def testValidMoves(self):
                """Tests that valid_moves returns correct positions"""
                # 'k' denotes a knight
                # 'x' denotes possible moves
                # Positions should be given in (row, column) tuples
                #  0 1 2 3 4 5 6 7      <---- y
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - x - - - - - -
                #6 - - x - - - - -
                #7 k - - - - - - -
                #^
                #|
                #x

                # TODO: Fill in the data to test valid_moves on the board above
                
                k_idx1 = (7,0)
                expected_valid_moves = [(6,2), (5,1)]
                self.assertEqual(expected_valid_moves, valid_moves(k_idx1))

                # TODO: Write tests for valid_moves for the following boards
                #  0 1 2 3 4 5 6 7
                #0 k - - - - - - -
                #1 - - x - - - - -
                #2 - x - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx2 = (0,0)
                expected_valid_moves = [(1,2), (2,1)]
                self.assertEqual(expected_valid_moves, valid_moves(k_idx2))

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - k
                #1 - - - - - x - -
                #2 - - - - - - x -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx3 = (0,7)
                expected_valid_moves = [(2,6),  (1,5)]
                self.assertEqual(expected_valid_moves, valid_moves(k_idx3))

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - x -
                #6 - - - - - x - -
                #7 - - - - - - - k
                k_idx4 = (7,7)
                expected_valid_moves = [(6,5), (5,6)]
                self.assertEqual(expected_valid_moves, valid_moves(k_idx4))

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - x - x - - -
                #2 - x - - - x - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - x - x - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx5 = (3,3)
                expected_valid_moves = [(4, 5), (5, 4), (2, 5), (5, 2), (4, 1), (1, 4), (2, 1), (1, 2)]
                self.assertEqual(expected_valid_moves, valid_moves(k_idx5))

class TestSolveable(unittest.TestCase):
        def testUnsolveable(self):
                """Test a few unsolveable puzzles"""
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - x -
                #2 - - - - - - - -
                #3 - - - k - - - -
                #4 - - - - - x - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                p_idx1 = {(1,6),(4,5)}
                k_idx1 = (3,3)
                self.assertFalse(solveable(p_idx1, k_idx1))
                
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - x - - -
                #2 - x - - - - - -
                #3 - - - k - - - -
                #4 - - - - - x - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                p_idx2 = {(2,1),(1,4),(4,5)}
                k_idx2 = (3,3)
                #self.assertFalse(solveable(p_idx2, k_idx2))

        def testSolveableSimple(self):
                """Test a simple solveable puzzle"""
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - k - - -
                #4 - - - - - - x -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                p_idx1 = {(4,6)}
                k_idx1 = (3,4)
                self.assertTrue(solveable(p_idx1, k_idx1))
                
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - x - -
                #3 - - - k - - - -
                #4 - - - - - - x -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                p_idx2 = {(2,5),(4,6)}
                k_idx2 = (3,3)
                self.assertTrue(solveable(p_idx2, k_idx2))
                #  0 1 2 3 4 5 6 7
                #0 - - x x - - x -
                #1 - - - - x - x -
                #2 - - x x x - - x
                #3 - x - - x k - x
                #4 - - - x - x x x
                #5 - - - - x - x -
                #6 - - x x - - x -
                #7 - - - - - x - -
                #Extreme Test (went through a pathway which is further down in my unittests, and added one point that should not be possible)
                k_idx3 = (3, 5)
                p_idx3 = {(0,2),(0,3),(0,6),(1,4),(1,6),(2,2),(2,3),(2,4),(2,7),(3,1),(3,4),(3,7),(4,3),(4,5),(4,6),(4,7),(5,4),(5,6),(6,2),(6,3),(6,6),(7,5)}
                self.assertFalse(solveable(p_idx3, k_idx3))

        def testSolveableHard(self):
                """Test a few more complex solveable puzzles - try to break your recursive algorithm to help you catch any mistakes"""
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - - 
                #3 - - - k - - - -
                #4 - - - - - - - -
                #5 x - x - - - - -
                #6 - - - - - - - -
                #7 - x - - - - - -
                p_idx1 = {(5,0),(5,2),(7,1)}
                k_idx1 = (3,3)
                self.assertTrue(p_idx1, k_idx1)
                
                #  0 1 2 3 4 5 6 7
                #0 k - - - - - - -
                #1 - - - x - - - -
                #2 - x - - - - - -
                #3 - - - - x - - -
                #4 - x - - - - - -
                #5 - - - x - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                p_idx2 = {(1,3),(2,1),(3,4),(4,1),(5,3)}
                k_idx2 = (0,0)
                self.assertTrue(solveable(p_idx2, k_idx2))

                #  0 1 2 3 4 5 6 7
                #0 - - x x - - x -
                #1 - - - - x - x -
                #2 - - x x x - - x
                #3 - x - - x k - x
                #4 - - - x - x x x
                #5 - - - - x - x -
                #6 - - x - - - x -
                #7 - - - - - x - -
                #I like Chess - Test
                k_idx4 = (3, 5)
                p_idx4 = {(0,2),(0,3),(0,6),(1,4),(1,6),(2,2),(2,3),(2,4),(2,7),(3,1),(3,4),(3,7),(4,3),(4,5),(4,6),(4,7),(5,4),(5,6),(6,2),(6,6),(7,5)}
                self.assertTrue(solveable(p_idx4, k_idx4))
unittest.main()