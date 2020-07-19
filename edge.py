# Example:
# u = Vertex(x1, y1)
# v = Vertex(x2, y2)
# Undirected, so Edge(v, u) == Edge(u, v)
# e = Edge(v, u)

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __eq__(self, other): 
        # Overrides equality of two edge 
        # If it's the same class, then it should have the same vertices.
        if isinstance(other, Edge):
            return (other.u == self.v or other.u == self.u) and (other.v == self.u or other.v == self.v)

        # If it's not the same class, it's not equal
        return False

    def __repr__(self): 
        return "<{}-{}>".format(self.u, self.v)

    def __hash__(self): 
        return hash(repr(self))
