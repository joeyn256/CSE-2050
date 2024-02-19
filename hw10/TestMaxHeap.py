from MaxHeap import Entry, MaxHeap
import unittest, random, time
random.seed(658)

#TODO: Fill out any empty tests below
class TestEntry(unittest.TestCase):

    def test_gt_onepriority(self):
        """Tests Entry's with 1 priority"""
        e1=Entry(priority=[0],item="a")
        e2=Entry(priority=[1],item="b")
        self.assertTrue(e2>e1)
        # higher priority is weighted more

    def test_gt_threepriorities(self):
        """Tests Entries with with 3 priorities"""
        e1 = Entry(priority=[0, "c", 2], item="a") 
        e2 = Entry(priority=[0, "c", 3], item="b")
        self.assertTrue(e2>e1)
        # higher number is weighted more

    def test_gt_mismatchedpriorities(self):
        """Test comparisons b/w entries with different numbers of priorities"""
        e1 = Entry(priority=[0, 2], item="a") 
        e2 = Entry(priority=[0, 2, 3], item="b")
        self.assertTrue(e2>e1)
        # more numbers is weighted more

    def test_eq(self):
        """Test that items w/ exact same priorities are seen as equal"""
        e1 = Entry(priority=[0, 2], item="a") 
        e2 = Entry(priority=[0, 2], item="a")
        self.assertEqual(e1,e2)
        # two same entries weighted the same

class TestMaxHeap(unittest.TestCase):
    def test_add_remove_single(self):
        """Add a single item to the max heap, then remove it. This test is provided for you as an example."""
        e1 = Entry(priority=[0], item="a")
        mh = MaxHeap()
        self.assertEqual(len(mh), 0)
        mh.put(e1)
        self.assertEqual(len(mh), 1)
        self.assertEqual(mh.remove_max(), "a")
        self.assertEqual(len(mh), 0)

    def test_add_remove_random(self):
        """Add and remove many random items w/ same number of priorities"""
        mh=MaxHeap()
        for i in range(10):
            n = random.randint(1,20)
            s=str(n)
            e = Entry(priority=i,item=n)
            mh.put(e)
            # make sure number is added and length is updated
            self.assertEqual(len(mh), 1)
            mh.remove_max()
            #make sure number is properly removed
            self.assertEqual(len(mh), 0)


    def test_add_remove_several(self):
        """Add and remove several items with different numbers of priorities"""
        mh=MaxHeap()
        for i in range(100):
            m = 1001
            n = random.randint(1,1000)
            o = 0
            m_str=str(m)
            n_str=str(n)
            o_str=str(o)
            mh.put(Entry(priority=m,item=m_str))
            mh.put(Entry(priority=n,item=m_str))
            mh.put(Entry(priority=o,item=m_str))
            self.assertEqual(len(mh), 3)
            #tests that the first one removed has the highest priority
            self.assertEqual(mh.remove_max(), m_str)
            #length test make sure length is properly updated when removing the rest of the items
            self.assertEqual(len(mh), 2)
            mh.remove_max()
            self.assertEqual(len(mh), 1)
            mh.remove_max()
            self.assertEqual(len(mh), 0)
            
    def test_removefromempty(self):
        """Test Runtime error when removing from empty"""
        mh=MaxHeap()
        e1 = Entry(priority=[0], item="a")
        mh.put(e1)
        mh.remove_max()
        self.assertEqual(len(mh), 0)
        #raises RuntimeError if another item is attempted to be removed
        with self.assertRaises(RuntimeError) : mh.remove_max()

    # NOTE: This times heapify_up and _down, but does not test their functionality
def test_heapify(self):
        """Times heapify up and heapify down approaches. This 'test' provided for you"""
        print() # an extra blank line at the top
        
        # table header
        print('='*40)
        print(f"{'n':<10}{'t_h_up (ms)':<15}{'t_h_down (ms)':<15}"   )
        print('-'*40)

        # table body
        scalar = int(1E3)
        for n in [i*scalar for i in [1, 2, 3, 4, 5]]:
            t_h_up = 1000*time_f(MaxHeap, (list(range(n)), 'up'))
            t_h_down = 1000*time_f(MaxHeap, (list(range(n)), 'down'))
            print(f"{n:<10}{t_h_up:<15.2g}{t_h_down:<15.2g}")

        # table footer
        print("-"*40)   

def time_f(func, args, trials=5):
    """Returns minimum time trial of func(args)"""
    t_min = float('inf')

    for i in range(trials):
        start = time.time()
        func(*args)
        end = time.time()
        if end-start < t_min: t_min = end - start

    return t_min

unittest.main()

"""the  gt method in eq is not done
everything else should work altough it is ugly rn
and I'm missing a test or two"""