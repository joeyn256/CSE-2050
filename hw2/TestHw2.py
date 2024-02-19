# Start here. Once you have good test, move on to hw2.py

import unittest
from hw2 import Card, Deck, is_group
class TestCard(unittest.TestCase):
    def test_init(self):
        c1 = Card(2, "green", "striped", "diamond")
        
        self.assertEqual(c1.number, 2)
        self.assertEqual(c1.color, "green")
        self.assertEqual(c1.shading, "striped")
        self.assertEqual(c1.shape, "diamond")
        
    def test_str(self):
        c1 = Card(2, "green", "striped", "diamond")
        self.assertEqual(str(c1), "Card(2, green, striped, diamond)")

        #test that we can get a good string representation of GroupCard instances 
    def test_eq(self):
        c1 = Card(2, "green", "striped", "diamond")
        c2 = Card(2, "green", "striped", "diamond")

        self.assertTrue(c1 == c2)
        #Tests that two cards are equal iff all attributes (number, color, shading, shape) are equal
        

# Write your own docstrings for the tests below
class TestDeck(unittest.TestCase):
    def test_init(self):
        d1 = Deck()
        
        self.assertEqual(d1.my_nums, [1, 2, 3])
        self.assertEqual(d1.my_shapes, ['diamond', 'squiggle', 'oval'])
        self.assertEqual(d1.my_cols, ['green', 'blue', 'purple'])
        self.assertEqual(d1.my_shadings, ['empty', 'striped', 'solid'])
    
    def test_len(self):
        d1 = Deck()

        my_nums = [1, 2]
        my_shapes = ["circles", "squares", "ovals"]
        my_cols = ['maroon', 'aqua', 'perywinkle', 'blue']
        my_shadings = ['striped']
        d2 = Deck(numbers=my_nums, shapes=my_shapes, colors=my_cols, shadings=my_shadings)
        self.assertTrue(len(d1) == 81)
        self.assertTrue(len(d2) == 24)

    def test_draw_top(self):
        d1 = Deck()
        
        self.assertTrue(d1.draw_top(), Card(3, "purple", "solid", "oval"))
    def test_shuffle(self):

        d1 = Deck()
        self.assertNotEqual(d1.deck_list,d1.shuffle())

# After Card and Deck are working, write and test the alg below.
# Include a docstring.
class TestSimulator(unittest.TestCase):
    def test_is_group(self):
        c1 = Card(2, "green", "striped", "diamond")
        c2 = Card(1, "green", "solid", "diamond")
        c3 = Card(2, "green", "striped", "oval")
        c4 = Card(3, "blue", "empty", "squiggle")
        c5 = Card(1, "purple", "solid", "diamond")
        
        self.assertTrue(is_group(c1, c2, c3))
        self.assertTrue(is_group(c3, c4, c5))
        self.assertFalse(is_group(c1, c2, c4))

if __name__ == '__main__':
    unittest.main()
