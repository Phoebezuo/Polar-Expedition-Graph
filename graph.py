import math
import collections

from vertex import Vertex
from edge import Edge

inf = float('inf')

class EdgeAlreadyExists(Exception):
    def __init__(self, message):
        super().__init__(message)

class Graph:
    def __init__(self):
        self._vertices = []

    def insert_vertex(self, x_pos, y_pos):
        v = Vertex(x_pos, y_pos)
        self._vertices.append(v)
        return v

    def insert_edge(self, u, v):
        e = Edge(u, v)

        # Check that the edge doesn't already exist
        for i in u.edges:
            if i == e:
                # Edge already exists.
                raise EdgeAlreadyExists("Edge already exists between vertex!")

        # Add the edge to both nodes.
        u.add_edge(e)
        v.add_edge(e)

    def remove_vertex(self, v):
        # Remove it from the list
        del self._vertices[self._vertices.index(v)]

        # Go through and remove all edges from that node.
        while len(v.edges) != 0:
            e = v.edges.pop()
            u = self.opposite(e, v)
            u.remove_edge(e)

    @staticmethod
    def distance(u, v):
        # Euclidean Distance = sqrt( (x2-x1)^2 + (y2-y1)^2 )
        return math.sqrt(((v.x_pos - u.x_pos)**2) + ((v.y_pos - u.y_pos)**2))

    @staticmethod
    def opposite(e, v):
        # It must be a vertex on the edge.
        if v not in (e.u, e.v):
            return None

        if v == e.u:
            return e.v

        return e.u

    def find_emergency_range(self, v):
        max = self.distance(v, v)
        for u in self._vertices:
            if (self.distance(u, v)) > max:
                max = self.distance(u, v)
        return max

    def find_path(self, b, s, r):
        # distance from B to every vertex S in the path is within r

        if b == None or s == None:
            return 

        # initialize
        path = [b]
        storage = [path]

        while path and storage:
            path = storage.pop(0)
            cursor = path[-1]

            # base case
            if cursor == s:
                return path

            # recursive case
            for edge in cursor.edges:
                opposite = self.opposite(edge, cursor)

                if self.distance(opposite, b) <= r and opposite not in path:
                    new_path = list(path)
                    new_path.append(opposite)
                    storage.append(new_path)

    def minimum_range(self, b, s):
        # minimum range in the path to go from vertex B to vertex S

        if b == None or s == None: 
            return 

        # if b == s: 
        #     return D[s]

        # initialize algorithm
        D = {vertex: inf for vertex in self._vertices}
        D[b] = 0
        vertices = self._vertices.copy()
        visited = []

        # iteratively add vertices to S
        while vertices:
            cursor = min(vertices, key = lambda vertex : D[vertex])
            visited.append(cursor)

            if D[cursor] == inf: 
                break 

            for edge in cursor.edges:
                opposite = self.opposite(edge, cursor)

                if max(self.distance(opposite, b), D[cursor]) <= D[opposite] and opposite not in visited:
                    D[opposite] = max(self.distance(opposite, b), D[cursor])
            
            vertices.remove(cursor)
        return D[s]

    def move_vertex(self, v, new_x, new_y):
        # If there is already a vertex there, do nothing.
        for vertex in self._vertices:
            if vertex.x_pos == new_x and vertex.y_pos == new_y: 
                return 
        v.move_vertex(new_x, new_y)
