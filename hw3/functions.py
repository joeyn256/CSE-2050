import unittest

def t_const(L):
    return 2 * L # 1
# returns the double of an int, total n = 1, O(1)

def t_lin(L):
    min = float('inf') #2 1 for assigning min and another for creating a float
    for i in L: #n
        if i < min: #1
            min = i #1
    return min #1
# returns minimum of a list, total = n + 3, O(n)

def t_quad(L):
    duplicates = set() # 2 creating a new list and assigning
    for i in range(len(L)): #n
        for j in range(len(L)): #n
            if L[i] == L[j] and i != j: #2
                duplicates.add(L[j]) #2
    return duplicates # 1
# returns duplicates (if any) in a list, total = 4n^2 + 3, O(n^2)

if __name__ == "__main__":
    L1 = [5,6,5,-1,4,4,12]
    L2 = ['joey', 'kyle', 'joey', 'pete', 'jeff']
    a = 2

    assert t_const(a) == 4
    assert t_lin(L1) == -1
    assert t_quad(L1) == {4, 5}
    assert t_quad(L2) == {'joey'}


    





