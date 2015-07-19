import unittest


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    @classmethod
    def node_with_children(cls, val, left, right):
        node = cls(val)
        node.left = left
        node.right = right
        return node


def check_leaves_levels(root):
    """
    Check if all leaves are at the same level
    http://www.geeksforgeeks.org/check-leaves-level/
    """
    levels = []

    def depth_first_traversal(root, level):
        if not root:
            return

        if root.right is None and root.left is None:
            levels.append(level)
        else:
            depth_first_traversal(root.left, level + 1)
            depth_first_traversal(root.right, level + 1)

    depth_first_traversal(root, 0)
    return len(set(levels)) == 1


class CheckLeavesLevels(unittest.TestCase):
    def test_single_node(self):
        root = TreeNode('foo')
        self.assertTrue(check_leaves_levels(root))

    def test_same_level(self):
        """
                  12
                /
              5
            /   \
           3     9
          /      /
         1      2
        """
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode.node_with_children(3, node1, None)
        node9 = TreeNode.node_with_children(9, node2, None)
        node5 = TreeNode.node_with_children(5, node3, node9)
        root = TreeNode.node_with_children(12, node5, None)
        self.assertTrue(check_leaves_levels(root))

    def test_different_levels(self):
        """
            root
            / \
           1   2
          /
         3
        """
        node1 = TreeNode.node_with_children(1, TreeNode(3), None)
        node2 = TreeNode(2)
        root = TreeNode.node_with_children(0, node1, node2)
        self.assertFalse(check_leaves_levels(root))


if __name__ == '__main__':
    unittest.main()
