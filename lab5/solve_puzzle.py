
def solve_puzzle(L):
    visited = set()
    start = 0
    return _solve_puzzle(0, L, visited)

def _solve_puzzle(index, L, visited):
    if index == len(L) - 1:
        #This means zero at end is reached and we return true
        return True
    elif index in visited:
        #if we already visited the index then it is in a loop and we can't solve
        return False
    else:
        #Need to add the current index to the set to remember that we used it
        visited.add(index)
        #storing the new index value for the cw and ccw method to use in the near future
        c1 = (index + L[index]) % len(L)
        c2 = (index - L[index]) % len(L)

        cw = _solve_puzzle(c1, L, visited)
        #this function solves for closewise
        ccw = _solve_puzzle(c2, L, visited)
        #have to return clockwise or counterclockwise methods
        return cw or ccw
