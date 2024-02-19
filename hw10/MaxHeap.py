# TODO: init, gt, eq
class Entry:
    def __init__(self, priority, item):
        """ADD DOCSTRING"""
        self.priority = priority
        self.item = item

    def __gt__(self, other):
       """ADD DOCSTRING"""
       return self.priority > other.priority

    def __eq__(self, other):
        """ADD DOCSTRING"""
        if(self.priority == other.priority and self.item == other.item):
            return True

    # repr is provided for you
    def __repr__(self):
        """Returns string representation of an Entry """
        return f"Entry(priority={self.priority}, item={self.item})"



# TODO: _heapify_up, _heapify_down, put, remove_max
class MaxHeap:
    # init is provided for you, but you should modify the default heapify_direction value
    def __init__(self, items=None, heapify_direction='down'):
        """Initializes a new MaxHeap with optional collection of items"""
        self._L = []

        # if a collection of items is passed in, heapify it
        if items is not None:
            self._L = list(items)
            if heapify_direction == 'up': self._heapify_up()

            elif heapify_direction == 'down': self._heapify_down()

            else: raise RuntimeError("Replace heapify_direction default with 'up' or 'down' instead of None")

    def _heapify_up(self):
        """Heapifies self._L in-place using only upheap"""
        L=self._L
        i=0
        item= L[i]
        parent=self._parent(i)
        if i>0 and L[i] >L[parent]:
            self._swap(i,parent)
            self._upheap(parent)


    def _heapify_down(self):
        """Heapifies self._L in-place using only downheap"""
        L = self._L
        i = 0
        while True:
            left = self._left(i)
            right = self._right(i)
            large = i
            if large == i:
                break
            if left < len(L) and L[left] > L[large]:
                large = left
            if right < len(L) and L[right] > L[large]:
                large = right
            L[i], L[large] = L[large], L[i]
            i = large



    def put(self, entry):
        """ADD DOCSTRING"""
        self._L.append(entry)
        self._heapify_up

    def remove_max(self):
        """ADD DOCSTRING"""
        L=self._L
        if len(self._L) == 0:
            raise RuntimeError("Empty Heap")
        else:
            L[0], L[-1] = L[-1], L[0]
            max = L.pop()
            self._heapify_down()
            return max.item

    # len is number of items in PQ
    def __len__(self):
        """Number of items in PQ"""
        return len(self._L)

    #TODO: Add any private helper functions (e.g. _left, _right, _upheap, ...) below
    def _parent(self,i):
        return (i) // 2

    def _left(self,i):
        return 2 * i + 1

    def _right(self,i):
        return 2 * i + 2

    def _swap(self, a, b):
        L = self._L
        L[a], L[b] = L[b], L[a]

    def _children(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._L), right + 1))

    def _upheap(self,i):
        L=self._L
        item= L[i]
        parent=self._parent(i)
        if i>0 and L[i] >L[parent]:
            self._swap(i,parent)
            self._upheap(parent)

    def _downheap(self,i):
        left = self._left(i)
        right = self._right(i)
        L = self._L
        i = 0
        while True:
            large = i
            if large == i:
                break
            if left < len(L) and L[left] > L[large]:
                large = left
            if right < len(L) and L[right] > L[large]:
                large = right
            L[i], L[large] = L[large], L[i]
            i = large