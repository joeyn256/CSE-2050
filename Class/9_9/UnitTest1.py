import unittest

from Person import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.s1 = Student('jas14034', 'jake')
    
    def test_init(self):
        #assert s1.name == 'Jake'
        self.assertEqual(self.s1.get_name(), 'jake')
        self.assertEqual(self.s1.get_netid(), 'jas14034')
        #self.assertTrue()
        #self.assertAlmostEqual

    def test_change_name(self):
        self.assertEqual(self.s1.get_name(), 'jake')
        self.s1.set_name('marco')
        self.assertEqual(self.s1.get_name(), 'marco')

    def test_add_course(self):
        self.s1 = Student('jas14034', 'jake')

    def test_(self): pass

unittest.main()