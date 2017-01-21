import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_binary_search_tree_(root):
    return is_bst(root)


def is_bst(root, min=None, max=None):
    if not root:
        return True
    else:
        return all([
            is_bst(root.left, min, root.data),
            is_bst(root.right, root.data, max),
            root.data > min if min else True,
            root.data < max if max else True
        ])


class IsBSTTest(unittest.TestCase):

    def test_empty_tree(self):
        self.assertTrue(check_binary_search_tree_(None))

    def test_root_with_no_childs(self):
        root = Node(1)
        self.assertTrue(check_binary_search_tree_(root))

    def test_root_with_only_left_child(self):
        root = Node(2)
        root.left = Node(1)
        self.assertTrue(check_binary_search_tree_(root))

    def test_root_with_only_right_child(self):
        root = Node(1)
        root.right = Node(2)
        self.assertTrue(check_binary_search_tree_(root))

    def test_smaller_left_grandchild(self):
        """
            2
              3
            1   5
        """
        root = Node(2)
        root.right = Node(3)
        root.right.left = Node(1)
        self.assertFalse(check_binary_search_tree_(root))

    def test_smaller_left_grand_grandchild(self):
        """
            12
              15
            11
           9
        """
        root = Node(10)
        root.right = Node(15)
        root.right.left = Node(11)
        root.right.left.left = Node(9)
        self.assertFalse(check_binary_search_tree_(root))


if __name__ == '__main__':
    unittest.main()
