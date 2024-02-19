class Graph:
    def __init__(self, V = set(), E=()):
        self.V = V
        self.E=dict()
        for u,v,wt in E:
            self.add_edge(u,v,wt)

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, u, v, wt):
        if u in self.E:
            self.E[u][v]=wt
        else:
            self.E[u]={v:wt}
        if v in self.E:
            self.E[v][u]=wt
        else:
            self.E[v]={u:wt}

    def remove_edge(self, u, v, wt):
        del self.E[u][v]
        del self.E[v][u]

        if len(self.E[u])==0:
            self.E.pop(u)
    def __iter__(self):
        return iter(self.V)

    def nbrs(self, v):
        return iter(self.E[v])

    def __len__(self):
        return len(self.V)

    def bfs(self, v): # BFS Tree
        tree = {}
        to_visit = [(None, v)]
        while to_visit:
            a, b = to_visit.pop(0)
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    to_visit.append((b,n))
        return tree

    def dfs_iter(self, v): # DFS_Iter Tree
        tree = {}
        to_visit = [(None, v)] # parent child
        while to_visit:
            a, b = to_visit.pop()
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    to_visit.append((b,n))
        return tree

    def dfs(self, v): #DFS Tree
        tree = {v:None}
        return self._dfs(v,tree)

    def _dfs(self, v, tree):
        for n in self.nbrs(v):
            if n not in tree:
                tree[n] = v
                return self._dfs(n,tree)
        return tree

    def fewest_flights(self, city):
        bfs1 = self.bfs(city) #store a BFS tree to reference (needed for this problem)
        maxpaths = 0
        for a in bfs1:
            counter = 0 #Keep track of how many paths each take to get bavck to New York (the city you are seeing how far each is from it)
            c = True
            while c == True: #Keep C True as long as the path does not end in None which is reversing the child parent order and updating the counter until the Path None is reach (which is connected to New York)
                if (bfs1[a] is not None): #This solution goes through all the paths in the dictionary and uses a counter to see how many paths each takes
                    counter += 1 # if there is a pathway that does not end in None counter goes up by one
                    a = bfs1[a] 
                    if counter > maxpaths:#checks and updates the max distance to any of the cities if the counter is greater than maxpaths
                        maxpaths = counter
                else:
                    c = False
        return maxpaths, self.bfs(city) # return the maxpaths to get to the furthest travesed city, and return the BFS tree that was traversed


    def shortest_path(self, city):
        bfs1 = self.bfs(city) # Storing the BFS to reference later
        dict1 = {} # store a new dictionary that will return the cities connected with the value as the miles between shortest path
        for i in bfs1:
            if bfs1[i] == city and bfs1[i] != None: #if there is a direct nonnection between the city then add that to the dictionary
                dict1[i] = self.distance(i, bfs1[i]) #add a key:value pair in dictionary with the key as the city connected, and value as the number of miles to the city from the city you are searching for
            elif bfs1[i] in dict1: #if there is not a direct connection, since I am using BFS there should be a connection prior to the original city, so I will search for that using memoization in my new dictionary and then add that entry
                dict1[i] = self.distance(i, bfs1[i]) + dict1[bfs1[i]] #add the key:value pair and add the distance between the city to the next closest city and add that with the closest connection (in miles) already found prior using memoization
                #used elif because there should be prior connections due to how BFS works (should not add if there are not)
        return dict1 #return key:value pairs with the cities and closest connections



    def distance(self, city1, city2): #made custom function to find distance between two cities
        return self.E[city1][city2]

    def minimum_salt(self, city):
        tot1 = 0 #this will be used to sum up the total distances
        dfs1 = self.dfs(city) #store dfs as a dict
        for i in self.dfs(city): #iterate through all elements
            if dfs1[i] != None: #this ignores how the first element is connected to none
                tot1 = tot1 + self.distance(i, dfs1[i]) #using my distance method, finds how many miles each two cities are connected to each other

        tot2 = 0
        dfs_iter1 = self.dfs_iter(city) #store dfs_iter as a dict and perfrom same function as above but for dfs_iter
        for i in self.dfs_iter(city):
            if dfs_iter1[i] != None: 
                tot2 = tot2 + self.distance(i, dfs_iter1[i]) 

        return min(tot1,tot2)  # return the minimum of the two DFS methods (DFS and DFS_iter) to find the minimum that connects all the cities