# TODO: implement the following 3 functions. Use docstrings, whitespace, and comments.

def cocktail_sort(a): 
#uses bubble_sort to sort L in-place
    n = len(a)
    swap = True
    start = 0
    end = n-1
    while (swap==True):
        # reset swap because it might be true
        swap = False
        # this is just a bubble sort left to right
        for i in range (start, end):
            if (a[i] > a[i+1]):
                a[i], a[i+1]= a[i+1], a[i]
                swap=True
        # if nothing moved, then array is sorted.
        if (swap==False):
            break
        #need to reset swap to go the other way
        swap = False
        # move the endpoint back to one and the end item is in its right spot now
        end = end-1
        # from right to left do the bubble sort but in the opposite direction
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        #swap index is in the right place so add 1 to start
        start = start+1
    return a

def bs_sublist(L, left, right, item):
# how to get the middle index of the sublist
    median = (right + left) // 2
#base cases
    if left == right:
        if L[left] > item:
            return left - 1
        elif L[left] == item:
            return left - 1
        else:
            return left
 
# if you arrive at the item (print index)
    if L[median] == item:
        return median - 1

 # search left and right 
    if L[median] < item:
        return bs_sublist(L, left+1, right, item)
    elif L[median] > item:
        return bs_sublist(L, left, right-1, item)

def opt_insertion_sort(L):
    n = len(L)
    newlist = [L[0]]
    for j in range(1, n):
        value = L[j]
        pos = bs_sublist(L, 0, j, value)
        newlist.insert(value, pos)
    return newlist
        

def insertion_sort(L):
    """Naive insertion sort. Adaptive, but still slow."""
    n = len(L)
    for j in range(n): # go through every item
        for i in range(n - 1 - j, n - 1): # bubble it into a sorted sublist
            if L[i] > L[i+1]:                 # 1 comparison
                L[i], L[i+1] = L[i+1], L[i]   # 2 writes 
            else: break
    