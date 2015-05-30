import unittest

"""
   Problem 4.1
   -----------------------------------------------------
   Implement a function to check if a tree is balanced.
   For the purposes of this question, a balanced tree is
   defined to be a tree such that no two leaf nodes differ
   in distance from the root by more than one.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def build_tree(cls, val, left, right):
        tree = cls(val)
        tree.left = left
        tree.right = right
        return tree


def is_balanced(root):
    max_pathsum = None
    min_pathsum = None
    frontier = [(root, 0)]

    if root is None:
        return True

    while frontier:
        current, pathsum = frontier.pop()
        if not current.left and not current.right:
            if max_pathsum is None or pathsum > max_pathsum:
                max_pathsum = pathsum

            if min_pathsum is None or pathsum < min_pathsum:
                min_pathsum = pathsum
        else:
            if current.right:
                frontier.append((current.right, pathsum + 1))
            if current.left:
                frontier.append((current.left, pathsum + 1))

    return max_pathsum - min_pathsum <= 1


class TestIsBalanced(unittest.TestCase):

    def test_null_tree(self):
        self.assertTrue(is_balanced(None))

    def test_right_balanced(self):
        """
        Balanced to the right test

                1
              /  \
             2    3
            /    /  \
           4    5    6
                      \
                       7
        """

        # leaves
        node7 = TreeNode(7)
        node5 = TreeNode(5)
        node4 = TreeNode(4)

        node6 = TreeNode.build_tree(6, None, node7)
        node3 = TreeNode.build_tree(3, node5, node6)
        node2 = TreeNode.build_tree(2, node4, None)
        root = TreeNode.build_tree(1, node2, node3)

        self.assertTrue(is_balanced(root))

    def test_left_balanced(self):
        """
        Balanced to the left test

                    1
                  /  \
                 2    3
                /    /  \
               4    5    6
             /
            7
        """

        # leaves
        node7 = TreeNode(7)
        node5 = TreeNode(5)
        node4 = TreeNode(6)

        node6 = TreeNode.build_tree(4, node7, None)
        node3 = TreeNode.build_tree(3, node5, node6)
        node2 = TreeNode.build_tree(2, node4, None)
        root = TreeNode.build_tree(1, node2, node3)

        self.assertTrue(is_balanced(root))

    def test_leaf(self):
        """
        Leaf test
            1
             \
              2
        """
        node2 = TreeNode(2)
        root = TreeNode.build_tree(1, None, node2)
        self.assertTrue(is_balanced(root))

    def test_unbalanced(self):
        """
        Unbalanced test
            1
           / \
          4   2
                \
                 3
                  \
                   5
        """
        node5 = TreeNode(3)
        node4 = TreeNode(4)
        node3 = TreeNode.build_tree(3, None, node5)
        node2 = TreeNode.build_tree(2, None, node3)
        root = TreeNode.build_tree(1, node4, node2)
        self.assertFalse(is_balanced(root))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsBalanced)
    unittest.TextTestRunner(verbosity=2).run(suite)
