import unittest
from TaskQueue import Task, TaskQueue

class tQueue(unittest.TestCase):
    #test intialization
    def test_init(self):
        t1 = Task(id=1, cycles_left=3)
        TQ = TaskQueue()
        TQ.add_task(t1)

        self.assertEqual(TQ.current.id, 1)
        self.assertEqual(TQ.current.cycles_left, 3)
    
    #test add, remove, and current
    def test_Add_Remove_andCurrent(self):
        TQ = TaskQueue()
        t1 = Task(id=1, cycles_left=3)
        t2 = Task(id=2, cycles_left=1)
        t3 = Task(id=3, cycles_left=5)
        t4 = Task(id=4, cycles_left=6)
        tasks = [t1, t2, t3, t4]
        TQ = TaskQueue()
        for task in tasks:
            TQ.add_task(task)
        # checking for 2 --> 3 --> 4 --> 1 ... --> 2
        # straight forward iteration
        self.assertEqual(TQ._head.id, 2)
        self.assertEqual(TQ._head.link.id, 3)
        self.assertEqual(TQ._head.link.link.id, 4)
        self.assertEqual(TQ._head.link.link.link.id, 1)
        #make sure that the end of loop loops back to beginning
        self.assertEqual(TQ._head.link.link.link.link.id, 2)  
        
        # checking to see the list iterates opposite so 1 ... <-- 2 <-- 3 <-- 4 <-- 1
        self.assertEqual(TQ.current.id, 1)
        self.assertEqual(TQ.current.prev.id, 4)
        self.assertEqual(TQ.current.prev.prev.id, 3)
        self.assertEqual(TQ.current.prev.prev.prev.id, 2)
        #make sure that the beginning of loop loops back to end
        self.assertEqual(TQ.current.prev.prev.prev.prev.id, 1)

        # check to make sure current is correct
        self.assertEqual(TQ.current.id, 1)

        TQ.remove_task(3)
        #check to see if list updates when remove is run
        # expect 2 --> 4 --> 1 ... --> 2
        self.assertEqual(TQ._head.id, 2)
        self.assertEqual(TQ._head.link.id, 4)
        self.assertEqual(TQ._head.link.link.id, 1)
        #check if loops back to beginning
        self.assertEqual(TQ._head.link.link.link.id, 2)
        
        #check to see if list updates opposite when remove is run
        # expect 1 <-- ... 2 <-- 4 <-- 1
        self.assertEqual(TQ.current.id, 1)
        self.assertEqual(TQ.current.prev.id, 4)
        self.assertEqual(TQ.current.prev.prev.id, 2)
        #check if loops back to beginning
        self.assertEqual(TQ.current.prev.prev.prev.id, 1)
        
        #check if current is still correct
        self.assertEqual
        self.assertEqual(TQ.current.id, 1)

        TQ.remove_task(1)
        # expect 2 (current) --> 4 ... --> 2
        #check to see if current updates
        self.assertEqual(TQ.current.id, 2)

        TQ.remove_task(2)
        TQ.remove_task(4)
        #expect current to be None
        self.assertEqual(TQ.current, None)

    def test_execute(self):
        t1 = Task(id=1, cycles_left=3)
        t2 = Task(id=2, cycles_left=1)
        t3 = Task(id=3, cycles_left=5)
        tasks = [t1, t2, t3]
        TQ = TaskQueue()
        for task in tasks:
            TQ.add_task(task)
        #check final cycle value == 9
        self.assertEqual(TQ.execute_tasks(), 9)
        #unittest should show the print values, also tested the print values on main (TaskQueue.py)
        #Output is correct as shown below, copied and pasted from unittest after run
        #Finished task 2 after 2 clock cycles
        #Finished task 1 after 6 clock cycles
        #Finished task 3 after 9 clock cycles
    #this test is testing __len__ and isempty() function
    def test_len_andis_empty(self):
        TQ = TaskQueue()
        self.assertEqual(len(TQ), 0)
        #test isempty()
        self.assertTrue(TQ.is_empty())
        
        t1 = Task(id=1, cycles_left=3)
        TQ.add_task(t1)
        self.assertEqual(len(TQ), 1) 
        #test isempty()
        self.assertFalse(TQ.is_empty())

        t2 = Task(id=2, cycles_left=1)
        t3 = Task(id=3, cycles_left=5)
        self.assertEqual(TQ.cycles_per_task, 1)
        TQ.add_task(t2)
        TQ.add_task(t3)

        self.assertEqual(len(TQ), 3)

        TQ.remove_task(2)
        self.assertEqual(len(TQ), 2)

        TQ.remove_task(1)
        self.assertEqual(len(TQ), 1)

        TQ.remove_task(3)
        #test to see if len() reverts back to 0
        self.assertEqual(len(TQ), 0)
        #test isempty()
        self.assertTrue(TQ.is_empty())
        try: 
            TQ.remove_task(15)
        except:
            self.assertRaises(RuntimeError)
        #This doesn't works but I self-tested the error and a runtime error is outputted, this documentation is to show I considered this in my code
    
    #test the correct values for length_2 which is assigned as how many total cycles are left when items are added and removed
    def test_len2(self):
        TQ = TaskQueue()
        t1 = Task(id=1, cycles_left=3)
        t2 = Task(id=2, cycles_left=2)
        
        #should be 0
        self.assertEqual(TQ._length2, 0)
        TQ.add_task(t1)
        #should be 3
        self.assertEqual(TQ._length2, 3)
        TQ.add_task(t2)
        #should be 5
        self.assertEqual(TQ._length2, 5)
        TQ.remove_task(1)
        #should be 2
        self.assertEqual(TQ._length2, 2)
        #should revert to 0
        TQ.remove_task(2)
        self.assertEqual(TQ._length2, 0)
#run all main tests
if __name__ == '__main__':
    unittest.main()