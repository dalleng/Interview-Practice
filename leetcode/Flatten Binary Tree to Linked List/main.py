import unittest

"""
Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if not root or (not root.left and not root.right):
            self.last = root
        else:
            if root.left:
                self.flatten(root.left)
                aux = root.right
                root.right = root.left
                root.left = None
                self.last.right = aux

            if root.right:
                self.flatten(root.right)


# 03/Jul/2021 alternative solution just returning a list of
# nodes in preorder and then iterating through it and setting
# the connections properly
class Solution2:
    def flatten(self, root: TreeNode) -> None:
        preorder = []

        def traversal(root):
            if not root:
                return
            preorder.append(root)
            traversal(root.left)
            traversal(root.right)

        traversal(root)

        for i in range(len(preorder)-1):
            preorder[i].right = preorder[i+1]
            preorder[i].left = None


# 03/Jul/2021 alternative solution using recursion and modifying
# the tree in place
class Solution3:
    def flatten(self, root: TreeNode) -> None:
        return self._flatten(root)

    def _flatten(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        left_tail = self._flatten(root.left)
        right_tail = self._flatten(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        return right_tail if right_tail else left_tail


def flattened_str(root):
    if not root:
        return ''

    s = '{}'.format(root.val)
    node = root
    while node:
        if node.right:
            s += ' -> {}'.format(node.right.val)
        node = node.right
    return s


class FlattenedTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_null(self):
        root = None
        self.solution.flatten(root)
        solution_str = flattened_str(root)
        self.assertEquals(solution_str, '')

    def test_problem_example(self):
        root = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        root.left = node2
        root.right = node5
        node2.left = node3
        node2.right = node4
        node5.right = node6

        self.solution.flatten(root)
        solution_str = flattened_str(root)

        self.assertEquals(solution_str, '1 -> 2 -> 3 -> 4 -> 5 -> 6')

    def test_large(self):
        """
                1
               / \
              2   5
             / \  / \
            3  4  9  6
               / \
              7   8
        """
        root = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node8 = TreeNode(8)
        node9 = TreeNode(9)

        root.left = node2
        root.right = node5
        node2.left = node3
        node2.right = node4
        node5.left = node9
        node5.right = node6
        node4.left = node7
        node4.right = node8

        self.solution.flatten(root)
        solution_str = flattened_str(root)

        self.assertEquals(solution_str,
                          '1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 5 -> 9 -> 6')

    def test_left_balanced(self):
        """
                1
               /
              2
             /
            3
           /
          4
        """
        root = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        root.left = node2
        node2.left = node3
        node3.left = node4

        self.solution.flatten(root)
        solution_str = flattened_str(root)

        self.assertEquals(solution_str, '1 -> 2 -> 3 -> 4')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FlattenedTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
