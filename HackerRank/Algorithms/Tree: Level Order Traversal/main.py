import unittest
from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    @classmethod
    def build_tree(cls, info, left, right):
        tree = cls(info)
        tree.left = left
        tree.right = right
        return tree

    def __str__(self):
        return str(self.info)


def levelOrder(root):
    result = ""
    frontier = deque([root])

    while frontier:
        current = frontier.popleft()
        if current.left:
            frontier.append(current.left)
        if current.right:
            frontier.append(current.right)
        result += f"{current.info} "

    print(result.strip())
    return result.strip()


class LevelOrderTest(unittest.TestCase):
    def test_basic(self):
        """
        1
        \
          2
           \
            5
            / \
            3   6
             \
              4
        """
        tree = Node.build_tree(
            1,
            None,
            Node.build_tree(
                2, None, Node.build_tree(5, Node.build_tree(3, None, Node(4)), Node(6))
            ),
        )
        self.assertEqual(levelOrder(tree), "1 2 5 3 6 4")

    def test_single_node_tree(self):
        tree = Node(8)
        self.assertEqual(levelOrder(tree), "8")


if __name__ == "__main__":
    unittest.main()
