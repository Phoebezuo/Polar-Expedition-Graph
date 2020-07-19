"""
Test File 1
-----------

Tests simple functions can be run UNIQUELY. It only calls one function at a time.

PLEASE NOTE: These tests are not equivalent to the tests run for grading,
they are only here to be used as a guideline!

To run this file, in your terminal from the folder above
(the one with edge.py, graph.py and vertex.py):

python3 -m unittest tests/test_single_functions.py

(or on some systems)

python -m unittest tests/test_single_functions.py
"""

import math
import unittest

from vertex import Vertex
from graph import Graph

# Tolerance for the threshold of distances
TOLERANCE_THRESHOLD=0.001

def approx_value(a, b):
    """
    Asserts that the value of a and b are approximately close.
    :param a: A number to compare to.
    :param b: A number to compare against.
    :return: The bool if they're approximate
    """

    return math.isclose(a, b, abs_tol=TOLERANCE_THRESHOLD)


def check_is_path(G, start, p, r):
    """
    Check that the path is indeed correct
    :param G: the graph
    :param start: The starting vertex.
    :param p: Path of vertices to visit.
    :param r: Range for the path
    :return bool if is a path
    """

    if p is None:
        return False

    # start the path with vertex 0
    current_v = p[0]
    next_in_path = 1

    while next_in_path < len(p):
        assert current_v is not None, "Found None in path: {}".format(p)
        # Get all the vertices in the edges:
        e_set = [G.opposite(e, current_v) for e in current_v.edges]
        assert p[next_in_path] in e_set, \
            """
            Your path ({}) includes non-existing edge
            from {} to {}.""".format(
                p,
                current_v,
                p[next_in_path]
            )

        assert G.distance(start, current_v) <= r, \
            """
            Vertex {} is outside range {} from start {}.
            Its range is {}""".format(
                current_v,
                r,
                start,
                G.distance(start, current_v)
            )
        current_v = p[next_in_path]
        next_in_path += 1

    assert current_v == p[-1], \
        "Your path ({}) didn't return a full path!".format(p)


class SingularFunctionTest(unittest.TestCase):
    """
    Tests one function at a time, to ensure that BASIC implementation
    has been completed.

    These tests should give you an understanding about HOW the graph
    is expected to work function by function.
    """

    ##################################################
    # Vertex: move_vertex
    ##################################################

    def test_can_move_vertex_once_from_vertex(self):
        """
        Tests that you have implemented the `move_vertex` from the vertex class.
        """

        v = Vertex(1, 1)

        # Check that the init has not changed.
        assert v.x_pos == 1 and v.y_pos == 1, "Vertex initialisation failed!"

        # Check that you can move it.
        v.move_vertex(2, 2)

        assert v.x_pos == 2, "Vertex X position didn't change! " + \
            "Expected: {}, Got: {}".format(2, v.x_pos)

        assert v.y_pos == 2, "Vertex Y position didn't change! " + \
                             "Expected: {}, Got: {}".format(2, v.y_pos)

    def test_can_move_vertex_n_times_from_vertex(self):
        """
        Test that we can call 'vertex.move_vertex' multiple times.
        """

        v = Vertex(1, 1)

        for i in range(2, 20):
            v.move_vertex(i, i-1)

            assert v.x_pos == i, "Vertex x_pos didn't change! " + \
                "Expected: {}, Got: {}".format(i, v.x_pos)

            assert v.y_pos == i-1, "Vertex y_pos didn't change! " + \
                                 "Expected: {}, Got: {}".format(i-1, v.y_pos)

    def test_can_move_more_than_one_vertex(self):
        """
        Can we move more than one vertex?
        """

        v1 = Vertex(1, 1)
        v2 = Vertex(2, 2)

        v1.move_vertex(4, 5)

        assert v1.x_pos == 4, "Vertex x_pos didn't change! " + \
                             "Expected: {}, Got: {}".format(4, v1.x_pos)

        assert v1.y_pos == 5, "Vertex y_pos didn't change! " + \
                              "Expected: {}, Got: {}".format(5, v1.y_pos)

        v2.move_vertex(6, 7)

        assert v2.x_pos == 6, "Vertex x_pos didn't change! " + \
                              "Expected: {}, Got: {}".format(6, v2.x_pos)
        assert v2.y_pos == 7, "Vertex y_pos didn't change! " + \
                              "Expected: {}, Got: {}".format(7, v2.y_pos)

    ##################################################
    # Graph: move_vertex
    ##################################################

    def test_graph_can_move_single_vertex(self):
        """
        Can we move the vertex by calling the Graph?
        """

        G = Graph()

        v = G.insert_vertex(1, 1)
        G.move_vertex(v, 3, 3)

        assert v.x_pos == 3, "Vertex x_pos didn't change! " + \
                             "Expected: {}, Got: {}".format(3, v.x_pos)

        assert v.y_pos == 3, "Vertex y_pos didn't change! " + \
                               "Expected: {}, Got: {}".format(3, v.y_pos)

    def test_graph_can_move_different_vertices(self):
        """
        Can we call more than one vertex to move?
        """

        G = Graph()

        v1 = G.insert_vertex(2, 3)
        v2 = G.insert_vertex(4, 5)

        G.insert_edge(v1, v2)

        G.move_vertex(v2, 6, 2)

        assert v2.x_pos == 6, "Vertex x_pos didn't change! " + \
                              "Expected: {}, Got: {}".format(6, v2.x_pos)

        assert v2.y_pos == 2, "Vertex y_pos didn't change! " + \
                              "Expected: {}, Got: {}".format(2, v2.y_pos)

        assert v1.x_pos == 2, "A different Vertex x_pos changed! " + \
                              "Expected: {}, Got: {}".format(2, v1.x_pos)

        assert v1.y_pos == 3, "A different Vertex y_pos changed! " + \
                              "Expected: {}, Got: {}".format(3, v1.y_pos)

        # Move v1 where v2 originally was
        G.move_vertex(v1, 4, 5)

        assert v1.x_pos == 4, "Vertex x_pos didn't change! " + \
                              "Expected: {}, Got: {}".format(5, v2.x_pos)

        assert v1.y_pos == 5, "Vertex y_pos didn't change! " + \
                              "Expected: {}, Got: {}".format(5, v2.y_pos)

        assert v2.x_pos == 6, "A different Vertex x_pos changed! " + \
                              "Expected: {}, Got: {}".format(6, v1.x_pos)

        assert v2.y_pos == 2, "A different Vertex y_pos changed! " + \
                              "Expected: {}, Got: {}".format(2, v1.y_pos)

    ##################################################
    # Graph: Find Emergency Range
    ##################################################

    def test_can_find_emergency_range(self):
        """
        Can we find the emergency range with just one other vertex in the graph?
        """

        G = Graph()

        v = G.insert_vertex(1, 2)
        v2 = G.insert_vertex(4, 10)

        G.insert_edge(v, v2)

        res = G.find_emergency_range(v)
        expected_value = 8.54400

        assert approx_value(res, expected_value), \
            "Expected: {} Got: {}".format(expected_value, res)

    def test_can_find_emergency_range_connected_vertex(self):
        """
        Can we find the emergency range with a number of vertex.
        """

        G = Graph()
        v = G.insert_vertex(0, 0)
        v1 = G.insert_vertex(1, 1)
        v2 = G.insert_vertex(9, 3)
        v3 = G.insert_vertex(2, 7)
        v4 = G.insert_vertex(5, 3)

        G.insert_edge(v, v1)
        G.insert_edge(v, v2)
        G.insert_edge(v, v4)
        G.insert_edge(v2, v3)
        G.insert_edge(v4, v3)
        G.insert_edge(v2, v4)

        res = G.find_emergency_range(v)
        expected_value = 9.48683

        assert approx_value(res, expected_value), \
            "Expected: {} Got: {}".format(expected_value, res)

        res = G.find_emergency_range(v3)
        expected_value = 8.06226

        assert approx_value(res, expected_value), \
            "Expected: {} Got: {}".format(expected_value, res)

        res = G.find_emergency_range(v2)
        expected_value = 9.48683

        assert approx_value(res, expected_value), \
            "Expected: {} Got: {}".format(expected_value, res)


    ##################################################
    # Graph: Find Path
    ##################################################

    def test_can_find_path_two_vertices_only(self):
        """
        Can we find a path of just

        A--B
        """

        G = Graph()

        b = G.insert_vertex(1, 2)
        s = G.insert_vertex(4, 10)

        G.insert_edge(b, s)

        r = 10
        r_path = G.find_path(b, s, r)

        check_is_path(G, b, r_path, r)

        assert r_path[0] == b, "Path did not start from starting vertex!"
        assert r_path[-1] == s, "Path did not end at destination vertex!"

    def test_can_find_path_for_graph_within_range(self):
        """
        Can we find a path of a simple graph

                A
              / | \
             B  C  D
               / | /
              E   F
        """

        G = Graph()

        # Layer 1
        A = G.insert_vertex(0, 0)

        # Layer 2
        B = G.insert_vertex(2, 0)
        C = G.insert_vertex(2, 4)
        D = G.insert_vertex(2, 6)

        # Layer 3
        E = G.insert_vertex(3, 3)
        F = G.insert_vertex(4, 6)

        # Make the edges
        G.insert_edge(A, B)
        G.insert_edge(A, C)
        G.insert_edge(A, D)
        G.insert_edge(C, E)
        G.insert_edge(C, F)
        G.insert_edge(D, F)

        # Now get the path
        r = 7.7
        p = G.find_path(A, F, r)

        check_is_path(G, A, p, r)

        assert A == p[0], "Path did not start at correct vertex in G.find_path"
        assert F == p[-1], \
            "Path did not end at destination vertex in G.find_path"

    def test_returns_only_path_within_range(self):
        """
        Can we find a path of a simple graph

        Now, what if C is alllll the way out of the way
        Outside the specified range?

                A__________________________
              / |                         |
             B  D    __________________ C
                 | /
                 F
        """

        G = Graph()

        # Layer 1
        A = G.insert_vertex(0, 0)

        # Layer 2
        B = G.insert_vertex(2, 0)
        C = G.insert_vertex(2, 20)
        D = G.insert_vertex(2, 6)

        # Layer 3
        E = G.insert_vertex(3, 3)
        F = G.insert_vertex(4, 6)

        # Make the edges
        G.insert_edge(A, B)
        G.insert_edge(A, C)
        G.insert_edge(A, D)
        G.insert_edge(C, E)
        G.insert_edge(C, F)
        G.insert_edge(D, F)

        # Now get the path
        r = 7.7
        p = G.find_path(A, F, r)

        check_is_path(G, A, p, r)

        assert A == p[0], "Path did not start at correct vertex in G.find_path"
        assert F == p[-1], "Did not end at destination vertex in G.find_path"
        assert p == [A, D, F], "Did not find correct path"

    def test_does_find_minimal_hops_path(self):
        """
        Can we find a path of a simple graph

                A
              / | \
             B  H  D
               /| /
              E C-F
        """

        G = Graph()

        # Layer 1
        A = G.insert_vertex(0, 0)

        # Layer 2
        B = G.insert_vertex(2, 0)
        D = G.insert_vertex(2, 6)
        H = G.insert_vertex(1.5, 3)

        # Layer 3
        C = G.insert_vertex(2, 4)
        E = G.insert_vertex(3, 3)
        F = G.insert_vertex(4, 6)

        # Make the edges
        G.insert_edge(A, B)
        G.insert_edge(A, H)
        G.insert_edge(A, D)
        G.insert_edge(H, C)
        G.insert_edge(H, E)
        G.insert_edge(C, F)
        G.insert_edge(D, F)

        # Now get the path
        r = 7.7
        p = G.find_path(A, F, r)

        check_is_path(G, A, p, r)

        assert A == p[0], "Path did not start at correct vertex in G.find_path"
        assert F == p[-1], \
            "Path did not end at destination vertex in G.find_path"
        assert p == [A, D, F], "Path {} was not the shortest path".format(p)

    ##################################################
    # Graph: Minimum range
    ##################################################

    def test_find_minimum_range_simple_a_b(self):
        """
        Can we find the minimum range of only A--B
        (Two vertices)
        """

        G = Graph()

        A = G.insert_vertex(0, 0)
        B = G.insert_vertex(7, 7)

        G.insert_edge(A, B)

        expected = 9.89949
        res = G.minimum_range(A, B)

        assert approx_value(expected, res), \
            "[find_minimum_range] Expected: {} | Got: {}".format(expected, res)

    def test_find_minimum_range_simple_graph(self):
        """
        Find the minimum range
                A
              / | \
             B  C  D
               / | /
              E   F
        """

        G = Graph()

        # Layer 1
        A = G.insert_vertex(0, 0)

        # Layer 2
        B = G.insert_vertex(2, 0)
        C = G.insert_vertex(2, 4)
        D = G.insert_vertex(2, 6)

        # Layer 3
        E = G.insert_vertex(3, 3)
        F = G.insert_vertex(4, 6)

        # Make the edges
        G.insert_edge(A, B)
        G.insert_edge(A, C)
        G.insert_edge(A, D)
        G.insert_edge(C, E)
        G.insert_edge(C, F)
        G.insert_edge(D, F)

        # Find the minimum range

        r = G.minimum_range(A, F)

        # quick maths.
        expected_r = 7.2111

        assert approx_value(expected_r, r), \
            "[find_minimum_range] Expected: {} | Got: {}".format(expected_r, r)

    def test_find_minimum_range_similar_paths(self):
        """
        Find the minimum range
                A
              / | \
             B  C  D
               / | /
              E   F
        """

        G = Graph()

        # Layer 1
        A = G.insert_vertex(0, 0)

        # Layer 2
        B = G.insert_vertex(2, 0)
        C = G.insert_vertex(2, 98)
        D = G.insert_vertex(2, 99)

        # Layer 3
        E = G.insert_vertex(3, 3)
        F = G.insert_vertex(4, 6)

        # Make the edges
        G.insert_edge(A, B)
        G.insert_edge(A, C)
        G.insert_edge(A, D)
        G.insert_edge(C, E)
        G.insert_edge(C, F)
        G.insert_edge(D, F)

        # Find the minimum range

        r = G.minimum_range(A, F)

        # quick maths.
        expected_r = 98.02041

        assert approx_value(expected_r, r), \
            "[find_minimum_range] Expected: {} | Got: {}".format(expected_r, r)

        G.remove_vertex(C)

        r = G.minimum_range(A, F)

        # quick maths.
        expected_r = 99.02041

        assert approx_value(expected_r, r), \
            "[find_minimum_range] Expected: {} | Got: {}".format(expected_r, r)
