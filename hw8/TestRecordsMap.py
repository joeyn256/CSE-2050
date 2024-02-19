from RecordsMap import *
import unittest, random
class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        new = LocalRecord(pos = (72.413,-54.324), max = 2, min = 1, precision = 0)
        self.assertEqual(new.pos, (72,-54))
        self.assertEqual(new.max, 2)
        self.assertEqual(new.min, 1)

    def test_hash(self):
        """ADD DOCSTRING"""
        hash1=LocalRecord((13,13))
        i=(13,13)
        self.assertEqual(hash1.__hash__(),1946675792496036303)
        self.assertEqual(hash1.__hash__(),hash(i))

    def test_eq(self):
        new1 = LocalRecord((71.444, -50.237))
        new2 = LocalRecord((71.001, -49.677))
        new3 = LocalRecord((71.501, -49.987))
        self.assertEqual(new1, new2)
        self.assertNotEqual(new1, new3)
    def test_add_report(self):
        """ADD DOCSTRING"""
        new1 = LocalRecord((71.444, -50.237), min = 1, max = 2)
        self.assertEqual(new1.min,1)
        self.assertEqual(new1.max,2)
        new1.add_report((123))
        new1.add_report((-51))
        self.assertEqual(new1.max,123)
        self.assertEqual(new1.min,-51)


class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """ADD DOCSTRING. Remember to test len, get, contains, and add_report"""
        RM= RecordsMap()
        p1=(12.3456,-12.3456)
        RM.add_report(p1,34)
        self.assertEqual(p1 in RM,True) #This tests if one case works
    def test_add_many_reports(self):
        """ADD DOCSTRING. Remember to test len, get, contains, and add_report"""
        RM= RecordsMap()
        p1=(-500,-31.5234)
        RM.add_report(p1,34)
        RM.add_report(p1,35)
        self.assertEqual(RM._len, 1)
        self.assertEqual(RM.__getitem__(p1), (34,35)) # tests that the values are updated if the same psoition is called which it is
        p2 = (1,2)
        RM.add_report(p2,1)
        p3 = (3,4)
        RM.add_report(p3,2)
        p4 = (5,6)
        RM.add_report(p4,3)
        self.assertEqual(len(RM._L),8)
        p5 = (7,8)
        RM.add_report(p5,4)
        self.assertEqual(RM._len, 5)
        self.assertEqual(len(RM._L),16)
        # Should rehash around here since i'm using length 8 for my buckets, if one rehashing works then it should always work
        p6 = (9,10)
        RM.add_report(p6,5)
        # did some testing with hashes and I expect p2 to be in 3, p3 in 5, p4 in 5, p5 in 14, p6 in 0, p7 in 0, and p8 in 1 which they are

if __name__ == '__main__':
    unittest.main()