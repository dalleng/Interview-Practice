import unittest
'''
Problem 4.2
-------------------------------------------------------
Given a directed graph, design an algorithm to find out
whether there is a route be- tween two nodes.
'''


def are_connected(graph, node1, node2):
    traversed = depth_first_traversal(graph, node1)
    if node2 in traversed:
        return True
    return False


def depth_first_traversal(graph, start):
    frontier = [start]
    visited = set()

    while frontier:
        current = frontier.pop()

        if current not in graph:
            continue

        for node in graph[current]:
            if node not in visited:
                frontier.append(node)
                visited.add(node)

    return visited


class AreConnectedTest(unittest.TestCase):
    def test_empty_graph(self):
        self.assertFalse(are_connected({}, 'foo', 'bar'))

    def test_non_existent_node(self):
        g = {1: [2]}
        self.assertFalse(are_connected(g, 2, 15))

    def test_directly_connected(self):
        g = {1: [2]}
        self.assertTrue(are_connected(g, 1, 2))
        self.assertFalse(are_connected(g, 2, 1))

    def test_non_connected_graph(self):
        g = {1: [2], 4: [3]}
        self.assertFalse(are_connected(g, 1, 4))
        self.assertFalse(are_connected(g, 1, 3))
        self.assertTrue(are_connected(g, 1, 2))
        self.assertTrue(are_connected(g, 4, 3))

    def test_loop(self):
        g = {1: [2], 2: [1]}
        self.assertTrue(are_connected(g, 1, 2))
        self.assertTrue(are_connected(g, 2, 1))

    def test_tree(self):
        """
            a
           / \
           b  c
          / \ /\
          d  e  f
        """
        g = {
            'a': ['b', 'c'],
            'b': ['d', 'e'],
            'c': ['e', 'f']
        }

        # The root has routes to all other nodes
        self.assertTrue(are_connected(g, 'a', 'b'))
        self.assertTrue(are_connected(g, 'a', 'c'))
        self.assertTrue(are_connected(g, 'a', 'd'))
        self.assertTrue(are_connected(g, 'a', 'e'))
        self.assertTrue(are_connected(g, 'a', 'f'))

        # Leaves have no routes to other nodes
        self.assertFalse(are_connected(g, 'd', 'b'))
        self.assertFalse(are_connected(g, 'd', 'e'))
        self.assertFalse(are_connected(g, 'd', 'f'))
        self.assertFalse(are_connected(g, 'd', 'c'))
        self.assertFalse(are_connected(g, 'd', 'a'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AreConnectedTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
