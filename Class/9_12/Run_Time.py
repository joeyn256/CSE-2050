def F1(a, b):
    if a > b:           #1
        return True     #1
    else:               #1
        return False    #1
                        #+___________
                        # 3 - worst case

def search(data, value):
    n = len(data)                   # 1 is that really 1 to find n, 1 to find len(data), 1 to store that in n? Maybe but one line of data we are just doing 1
    for index in range(n):          # n times
        if value == data[index]:    # 2
            return index            # 1
    return -1                       # 1
                                    #+______
                                    # 1 + n*(2) + 1 = 2n + 2

def nested_loops(n):        
    counter = 0             #1
    for i in range(n):      #n
        for j in range(n):  #n
            counter += 1    

    return counter          #1
                            # n*n*1 + 2 = n**2 + 2
