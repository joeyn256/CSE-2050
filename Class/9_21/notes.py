#input --> Black Box --> Output
#Deque add_first, add_last, rem_first, rem_last
#in a link-listed when a linked list points to None it is the end of the list
from symbol import pass_stmt
import xxlimited


class Node:
    def __init__(self,item, _next=None):
        self.item = item
        self._next = _next

if __name__ == '__main__':
    pass # test cases here
n1 = Node(3, None)
n2 = Node("hello", n1)
n3 = Node([1,2,3], n2)

try: pass
except:
    RuntimeError

# [1,2,3] --> "hello" --> 3