from BSTMap import BSTMap, BSTNode # provided for you

# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    # TODO: implement the three methods below
    def __eq__(self, other):

        return self.root == other.root #tells function what to start with

             # The heavy lifting here is done in the corresponding
             # function in MyBSTNode - just tell it which node to
             # start with.

    # these are "static" methods - they belong to the class but do not take an instance of 
    # the class as a parameter (no `self``).
    # note the "decorator" @staticmethod - this let's python know this is not a typical "bound" method
    @staticmethod
    def frompreorder(L):
        bst = MyBSTMap()

        for pairs in L: # generates a tree with pre-ordered key, value tuples
            bst.put(pairs.key, pairs.value)
            
        return bst

    @staticmethod
    def frompostorder(L):
        bst = MyBSTMap()

        L.reverse() #post order is the same thing as above but reversed
        
        for pairs in L: # generates a tree with pre-ordered key, value tuples
            bst.put(pairs.key, pairs.value)
        
        return bst

class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
    
        if self.key != other.key or self.value != other.value: #Check to see the actual values you are comparing equal each other for the key, value pair
            return False

        left_side = (self.left == other.left) #recursively the function for the left side
        right_side = (self.right == other.right) #resursively calls the function for the right side

        if left_side == False or right_side == False: #if one of these sides does not equal each other then return false
            return False

        else:
            return True # If false is not found then it is true!, pretty much the base case since it runs through all possibilities