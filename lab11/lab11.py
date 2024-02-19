class Graph_ES:
    def __init__(self, Vs = set(), Es = set()):
        self.V = Vs
        self.E = Es
    
    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, e):
        self.E.add(e)

    def remove_edge(self, e):
        self.E.remove(e)
    
    def __len__(self):
        return len(self.V)

    def _neighbors(self, v):
        nbrs = set()
        for e in self.E:
            if e[0] == v: nbrs.add(e[1])
        return nbrs


    def __iter__(self):
        return iter(self.V)


class Graph_AS:

    def __init__(self, Vs = set(), Es = set()):
        self.V = Vs
        self.E = Es
        # going to make the edges into dictionary elements that were originally intialized in unittests as a set
        dict_without_sets = dict(Es)
        #stores = {1:2, 2:1, 2:3, 3:2} but want {1:{2}, 2:{1}, 2:{3}, 3:{2}}
        self.nbrs = dict()
        #use the built in dictionary items() to make the dictionary we want with value pairs defined within a set
        for key,value in dict_without_sets.items():
            self.nbrs[key] = {value}
    
    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, e):
        a, b = e # e = (a,b)
        if a not in self.nbrs: 
           self.nbrs[a] = {b}
        else:
            self.nbrs[a].add(b)

    def remove_edge(self, e):
        a, b = e
        self.nbrs[a].remove(b)

        if len(self.nbrs[a]) == 0:
           self.nbrs.pop(a)
    
    def __len__(self):
        return len(self.V)

    def _neighbors(self, v):
        return iter(self.nbrs[v])

    def __iter__(self): 
        return iter(self.V)
