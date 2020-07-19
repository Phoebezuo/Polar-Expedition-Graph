class Vertex:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.edges = []

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return other.x_pos == self.x_pos and other.y_pos == self.y_pos
        return False

    def __ne__(self, other):
        if isinstance(other, Vertex):
            return other.x_pos != self.x_pos or other.y_pos != self.y_pos
        return True

    def __repr__(self):
        return "V({}, {})".format(self.x_pos, self.y_pos)

    def __hash__(self):
        return hash(repr(self))

    def add_edge(self, e):
        self.edges.append(e)

    def remove_edge(self, e):
        self.edges.remove(e)

    def move_vertex(self, x_pos, y_pos):
        self.x_pos = x_pos;
        self.y_pos = y_pos
