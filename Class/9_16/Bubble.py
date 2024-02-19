def is_sorted(L):
    """Returns a boolean representing whether L is sorted"""
    n = len(L)
    return not any(L[i] > L[i+1] for i in range(n-1))

def bubble_sort(L):
    """Sorts L using (an inefficient) bubble sort"""
    n = len(L) #1

    for i in range(n): #n
        for j in range(n-1): #n - 1
            if L[j] > L[j+1]: # 1
                L[j+1], L[j] = L[j], L[j +1] #1
                #when python sees commas it thinks of a tuple



if __name__ == '__main__':
    # Test is_sorted
    n = 500
    L = [i for i in range(n)]
    assert is_sorted(L)
    L[-1] = -1
    assert not is_sorted(L)

    bubble_sort(L)
    assert is_sorted(L)
    # fastest --> Slowest O(1), O(logn), O(n), O(nlogn), O(n^2), O(2^n)
    # f(n) = O(log,2,n) = O(log,5,n) = O(log,3,n)
    #log,2,8 = (log,4,8)/(log,4,2) = 3 ... log,a,b = (log,c,b)/(log,c,a)
    # any basic logirthim is some constant multiplied by a different log,c,n so any log base is equivalent
