def is_sorted(L):
    """Checks that L is monotonically increasing"""
    return not any(L[i] > L[i+1] for i in range(len(L) - 1))

def print_list(L, tab=False):
    """prints out L using rows of '=' to visualize item size"""
    for idx, item in enumerate(L):
        if tab: print("\t", end='')
        print(f"idx:{idx}", "="*item, f"{item}")
def bubble_sort(L): 
    """uses bubble_sort to sort L in-place"""
    n = len(L)
#  Invariant - something that is always true at some point in an algorithm

# at the end of i outer loops, the i biggest items are in their final positions
# at the end of (n-1) outer loops, the (n-1) biggest items are in their final positions
# at the end of (n-1) outer loops, only 1 item has not been sorted

# adaptive - running time depends on the input asymptoically

# worst case: O(n^2)
# best case: O(n)
    #when 1 big item at the front of our list "rabbit"
    #1 small item at the end: "turtle"
    for i in range(n):
        print(f"i={i}")
        print_list(L)
        input()

        for j in range(n-1-i):
            print(f"j={j}")
            print_list(L, tab=True)
            input()
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

            print_list(L, tab=True)
            input()
# at tye end of i outer loops, te i biggest items are in their final positions
def selection_sort(L):
    n = len(L)

    for i in range(n-1):
        #find the ith biggest item
        i_big = 0
        for j in range(n-i):
            print(f"j={j}")
            if L[j] > L[i_big]:
                i_big = j

        L[j], L[i_big] = L[i_big], L[j]

        print_list(L)
        input()

# selection
# n^2/2 comparisons
# 2n writes (still O(n^2) but spending a whole less time writing)

# bubble sort
# n^2/2 comparisons
# n^2/2 write operations




#after k outer loops, the final k items are sorted relative to each other
# they are not necessarily in their final positions
# [5,4,3,2,1]
# [5,4,3,2,1] after loop 1
# [5,4,3,1,2] after loop 2
# [5,4,1,2,3] after loop 3
# [5,1,2,3,4] after loop 4
# [1,2,3,4,5] after loop 5
def insertion_sort(L):
    #uses insetion sort to sort L in place
    #does same thing as bubble-sort but does it in the opposite order; This is extremely adapative but not as good as selection sort
    n = len(L)

    for i in range(n):
        for j in range(n-1-i, n-1):
            #store L[j] in a temp variable
            #shift items left until L[j] is smaller than item
            #write L[j] to remaining place
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
            else:
                break
            print(f"\tj={j}")
            print_list(L, tab=True)
            input()
# compares the smaller item at the end of the list to the next item and if that item is bigger than the bigger item is pushed all the way to the end of the list than after the list compares the smaller number versus the next and so on
    
    #when i = 0, j = _
    # when i = 1, 
    #   j = n - 2
    # when i = 2, 
    #   j = n-3
    #   j = n-2
    # when i = 3
    #   j = n-4
    #   j = n-3
    #   j= n -2

            
if __name__ == '__main__':
    """Tests sorting algorithms above"""
    import random

    ##### Test is_sorted() #####
    L = [i for i in range(10)]
   # L[0] = 10  doesn't have to be sorted
    assert is_sorted(L)
    L.append(2)
    assert not is_sorted(L)

    ##### Test bubble_sort() #####
    import random
    L = [random.randint(0,10) for i in range(10)]
    print(f"before sorting:")
    print_list(L)
    
    print(f"before sorting:")
    print_list(L)

    insertion_sort(L) #change this to test other sorts
    assert is_sorted(L)

    print(f"after sorting:")
    print_list(L)

    print("all done")