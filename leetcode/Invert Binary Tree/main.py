import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def nodeWithChildren(cls, val, left, right):
        node = cls(val)
        node.left = left
        node.right = right
        return node


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return root

        if not root.left and not root.right:
            return root
        else:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            aux = left
            root.left = right
            root.right = aux

            return root


class InvertTest(unittest.TestCase):
    def test_invert(self):
        s = Solution()
        node1 = TreeNode(1)
        node3 = TreeNode(3)
        node6 = TreeNode(6)
        node9 = TreeNode(9)
        node2 = TreeNode.nodeWithChildren(2, node1, node3)
        node7 = TreeNode.nodeWithChildren(7, node6, node9)
        node4 = TreeNode.nodeWithChildren(4, node2, node7)

        # Inverted tree
        node1_ = TreeNode(1)
        node3_ = TreeNode(3)
        node6_ = TreeNode(6)
        node9_ = TreeNode(9)
        node7_ = TreeNode.nodeWithChildren(7, node9_, node6_)
        node2_ = TreeNode.nodeWithChildren(2, node3_, node1_)
        node4_ = TreeNode.nodeWithChildren(4, node7_, node2_)

        s.invertTree(node4)

        self.assertEquals(node4.left.val, node4_.left.val)
        self.assertEquals(node4.right.val, node4_.right.val)
        self.assertEquals(node7.left.val, node7_.left.val)
        self.assertEquals(node7.right.val, node7_.right.val)
        self.assertEquals(node2.left.val, node2_.left.val)
        self.assertEquals(node2.right.val, node2_.right.val)


if __name__ == "__main__":
    unittest.main()
