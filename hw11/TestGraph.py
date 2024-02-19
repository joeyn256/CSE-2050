from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """ADD DOCSTRING"""
    #                               My Ascii Map
    #                       (1627 miles)    (1466 miles)
    #                  New York ----- Houston ----- Las Vegas
    #                     |                             |                  
    #                     |                             |
    #       (884 miles)   |                             |   (755 miles)
    #                     |                             |
    #                  Nashville  ------------------  Boulder
    #                                (1176 miles)
        v = {'New York', 'Houston', 'Las Vegas', 'Boulder',  'Nashville'}
        e = {('New York', 'Houston', 1627), ('Houston', 'New York', 1627), ('New York', 'Nashville', 884), ('Nashville', 'New York', 884),
        ('Houston', 'Las Vegas', 1466), ('Las Vegas', 'Houston', 1466), ('Las Vegas', 'Boulder', 755), ('Boulder', 'Las Vegas', 755),
        ('Boulder', 'Nashville', 1176), ('Nashville', 'Boulder', 1176)}
        self.g = Graph(v,e)
    def test_addremove_vertices(self):
        """Tests that we can add and remove vertices from graph"""
        self.assertEqual(len(self.g), 5) # should have 5 vertices

        self.g.remove_vertex('New York')
        self.assertEqual(len(self.g), 4) # should have 4 vertices

        self.g.add_vertex('Storrs')
        self.assertEqual(len(self.g), 5) # should have 5 vertices now

    def test_addremove_edges(self):
        """Tests that we can add and remove edges from graph"""
        # Initialliy, 1 is connected to 2
        n1 = {nbr for nbr in self.g.nbrs('New York')} # normally we wouldn't test private attributes
                                                   # we do so here since it's part of the assignment.
        self.assertEqual(n1, {'Nashville', 'Houston'})

        # add connection from 1-3
        self.g.add_edge('Storrs', 'New York', 141)
        n1 = {nbr for nbr in self.g.nbrs('Storrs')}
        self.assertEqual(n1, {'New York'})

        # remove connection 1-2
        self.g.remove_edge('Las Vegas', 'Houston', 1466)
        n1 = {nbr for nbr in self.g.nbrs('Las Vegas')}
        self.assertEqual(n1, {'Boulder'}) #Now Las Vegas should only be connected to Boulder
    
    def test_iter(self):
        """Tests that iter() goes over vertices correctly"""
        vs = {v for v in self.g}
        self.assertEqual(vs, {'New York', 'Houston', 'Las Vegas', 'Boulder',  'Nashville'})

        # Note that order does not matter when comparing sets
        self.g.add_vertex('Storrs')
        vs = {v for v in self.g}
        self.assertEqual(vs, {'New York', 'Houston', 'Las Vegas', 'Boulder',  'Nashville', 'Storrs'})
        
    # TODO: Add unittests for public interface of Graph class (except traversal algs)
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
    #                               My Ascii Map
    #                       (1627 miles)    (1466 miles)
    #                  New York ----- Houston ----- Las Vegas
    #                     |                             |                  
    #                     |                             |
    #       (884 miles)   |                             |   (755 miles)
    #                     |                             |
    #                  Nashville  ------------------  Boulder
    #                                (1176 miles)
        self.v = {'New York', 'Houston', 'Las Vegas', 'Boulder',  'Nashville'}
        self.e = {('New York', 'Houston', 1627), ('Houston', 'New York', 1627), ('New York', 'Nashville', 884), ('Nashville', 'New York', 884),
        ('Houston', 'Las Vegas', 1466), ('Las Vegas', 'Houston', 1466), ('Las Vegas', 'Boulder', 755), ('Boulder', 'Las Vegas', 755),
        ('Boulder', 'Nashville', 1176), ('Nashville', 'Boulder', 1176)}
        self.g = Graph(self.v,self.e)
    # already tested all the attributes to the graph and it works
   
   
   
   
    # TODO: Which alg do you use here, and why?
    # Alg: BFS
    # I am finding the minimum paths by exploring the branching paths from New York in either direction
    # below I show how this works and that the minimum expected paths would be 2 to connect all cities to New York
    #               Nashville --> Boulder 
    #           /
    # New York 
    #           \
    #               Houston --> Las Vegas
    def test_fewest_flights(self):
        self.assertTrue(self.g.fewest_flights('New York'), 2)


    # TODO: Which alg do you use here, and why?
    # Alg: BFS
    # Why: You can follow the paths directly backwards from New York (city you are using) muchlike how I was using this in the last part, I am just considering the distances now
    # I return a dictionary of all the cities and the shortest paths.
    def test_shortest_path(self):
        shortest_paths_from_New_York = {'Las Vegas': 3093, 'Houston': 1627, 'Nashville': 884, 'Boulder': 2060}
        # results should be = {('Boulder', 1176), ('Houston', 3093), ('Houston', 1627), ('Nashville', 884), ('Nashville', 2060), ('Las Vegas', 1466)}
        self.assertEqual(shortest_paths_from_New_York, self.g.shortest_path('New York'))



    # TODO: Which alg do you use here, and why?
    # Alg: DFS and DFS_iter
    # Why: since you have to find a path that connects all of the cities (these are the two methods we know to do that)
    
    def test_minimum_salt(self):
# dfs (New York) = {'New York': None, 'Houston': 'New York', 'Las Vegas': 'Houston', 'Boulder': 'Las Vegas', 'Nashville': 'Boulder'}
# dfs_iter (New York) = {'New York': None, 'Nashville': 'New York', 'Boulder': 'Nashville', 'Las Vegas': 'Boulder', 'Houston': 'Las Vegas'}
# dfs minimum would be 5024 (1627+1466+755+1176)
# dfs_iter minimium would be 4281 (884+1176+755+1466)
# since dfs_iter is the best path out of the two combinations we would expect that
        self.assertEqual(self.g.minimum_salt('New York'), 4281)

# dfs (Las Vegas) = {'Las Vegas': None, 'Houston': 'Las Vegas', 'New York': 'Houston', 'Nashville': 'New York', 'Boulder': 'Nashville'}
# dfs_iter (Las Vegas) + {'Las Vegas': None, 'Boulder': 'Las Vegas', 'Nashville': 'Boulder', 'New York': 'Nashville', 'Houston': 'New York'}
# dfs minimum would be 5153 (1466+1627+884+1176)
# dfs_iter minimum would be 4442
# since dfs_iter is the best path out of the two combinations we would expect that
        self.assertEqual(self.g.minimum_salt('Las Vegas'), 4442)

unittest.main()