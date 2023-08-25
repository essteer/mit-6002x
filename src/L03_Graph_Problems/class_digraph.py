# Adjacency matrix:
# - rows: source nodes
# - columns: destination nodes
# - cells[s, d] = 1 if there is an edge from s to d, else 0
# - do not have to be 1s and 0s, could be weighted, for example

# Adjacency list:
# - associate each node with a list of destination nodes

class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""

    def __init__(self):
        self.edges = {}

    def addNode(self, node):  # checks for errors, adds node if no errors
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()  # gets source node
        dest = edge.getDestination()  # gets source destination
        if not (src in self.edges and dest in self.edges):  # checks for errors
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)  # adds edge if no errors found

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                    + dest.getName() + '\n'
        return result[:-1]  # omit final newline
