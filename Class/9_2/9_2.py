L = [i for i in range(1000000)]
"asdf" in L
# false
-1 in L
# false

S = {i for i in range(1000000)}
-1 in S
# false
-1 in L
# false
-1 in S
# false
# we use hashes in sets and dictionaries, we don't store values but it is easy to look up values

S = {1,2,3,4}
D = {1:"one", 2:[1,2,3,4], 3:"asdf"}
# D command runs back that set
S.add(5) # adds 5 for S = {1,2,3,4,5}
S.add(1) # does not add any objects to S
# S would return {1,2,3,4,5}


