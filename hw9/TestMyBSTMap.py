import unittest, random
from MyBSTMap import MyBSTMap

class TestMyBSTMap(unittest.TestCase):
    def test_equal_empty(self):
        """ADD DOCSTRING"""
        A = MyBSTMap() # A is empty
        B = MyBSTMap() # B is empty
        self.assertTrue(A == B)

    def test_equal_multiplenodes(self):
        A = MyBSTMap()
        B = MyBSTMap()

        for i in [3,6,5,4,8,12,13]:
            A.put(i, str(i)) # generate A
            B.put(i, str(i)) # generate B
        self.assertEqual(A,B)
        """
        This is A and B
        3 -------           
       -- 6 -        
    -- 5     8 -     
    4          12 -  
                  13 
        """
        self.assertEqual(A,B) # check empty BSTMaps equal each other
         

    def test_notequal_multiplenodes_difshapes(self):
        """ADD DOCSTRING"""
        A = MyBSTMap()
        B = MyBSTMap()
        
        for i in [9,6,5,4,8,12,13,20,80,1,0]:
            A.put(i, str(i)) # generate A
        for i in [10,6,5,28,33,4,8,42,32,12,13]:
            B.put(i, str(i)) # generate B
        """
        This is for A
             ----- 9 -           
          -- 6 -     12 -        
       -- 5     8       13 -     
    -- 4                   20 -  
 -- 1                         80 
 0    
 This is for B      
        -----10 -------           
    -- 6 -      -----28 ----     
 -- 5     8    12 -      --33 -  
 4                13    32    42     
Different Shapes         
        """

        self.assertNotEqual(A,B) # run test

    def test_notequal_multiplenodes_difkvs(self):
        A = MyBSTMap()
        B = MyBSTMap()
        
        for i in [9,6,5,4,8,12,13]:
            A.put(i, str(i)) # generate A
        for i in [10,6,5,4,8,12,13]:
            B.put(i, str(i)) # generate B
        """ 
This is A
       ----- 9 -     
    -- 6 -     12 -  
 -- 5     8       13 
 4  

This is B
       -----10 -     
    -- 6 -     12 -  
 -- 5     8       13 
 4   
 Only one difference, should be a good test    
        """
        self.assertNotEqual(A,B) # test A is not equal to B


    def test_frompreorder_small(self):
        """ADD DOCSTRING"""
        A = MyBSTMap()
        B = MyBSTMap()

        for i in [45,30,20,10,55,15]:
            A.put(i, str(i)) # generate A
        """
        This is the tree A which should be Tree B
                  --45 -  
       --30    55 
 -----20          
10 -              
   15
        """
        preorderlist = [(key,value) for (key,value) in A.preorder()] #Executes preorder list

        self.assertNotEqual([(45, '45'), (30, '30'), (20, '20'), (10, '10'), (55, '55'), (15, '15')], preorderlist) # check if list used in A is different than B (which can happen by freak accident, but is very unlikely, probably 1/10000000 probability)

        for key, value in preorderlist: # adding the items into B after preorder is executed
            B.put(key,value) # create B
        
        self.assertEqual(A,B) # check if equal
    
    def test_frompreorder_large(self):
        """ADD DOCSTRING"""
        A = MyBSTMap()
        B = MyBSTMap()
        L = []
        for i in range(999):
            n = random.randint(0,999) # generate random variable in list
            
            L.append((n, str(n))) #remembering the list of random integers (for testing if preorder list prints something different)

            A.put(n, str(n)) # generate A

        preorderlist = [(key,value) for (key,value) in A.preorder()] # order items according to preorder

        self.assertNotEqual(L, preorderlist)
        
        for key, value in preorderlist: # adding the items into B after preorder is executed
            B.put(key,value) # generate B

        self.assertEqual(A,B) # check equality

    def test_frompostorder_small(self):
        """ADD DOCSTRING"""
        A = MyBSTMap()
        B = MyBSTMap()

        for i in [20,40,30,15, 300, 800]: #making random list
            A.put(i, str(i)) # generate A
        """
        Tree A should equal Table B
         --20 ----  
10     --40 
      30
        """

        postorderlist = [(key,value) for (key,value) in A.postorder()] #create postorder list
        
        postorderlist.reverse() # have to reverse the list to check to see if the list works when adding back to B

        for key, value in postorderlist: # adding the items into B after postorder is executed
            B.put(key,value) # generate B

        self.assertNotEqual([(20, '20'), (40, '40'), (30, '30'), (15, '15'), (300, '300'), (800, '800')], postorderlist) # check if post order list reversed differs from order of list added to A 
        
        self.assertEqual(A,B) # check equality


    def test_frompostorder_large(self):
        """ADD DOCSTRING"""
        A = MyBSTMap()
        B = MyBSTMap()
        L = []
        for i in range(999):
            n = random.randint(0,999) # generate random variable in list
            
            L.append((n, str(n))) #remembering the list of random integers (for testing if preorder list prints something different)

            A.put(n, str(n)) # generate A

        postorderlist = [(key,value) for (key,value) in A.postorder()] # order items according to post order
        postorderlist.reverse() # have to reverse the list to check to see if the list works when adding back to B

        self.assertNotEqual(L, postorderlist) # check if postorderlist reversed is not equal to the list (which can happen by freak accident, but is very unlikely, probably 1/10000000 probability)
        
        for key, value in postorderlist: # adding the items into B after preorder is executed
            B.put(key,value) # generate B

        self.assertEqual(A,B)

unittest.main()