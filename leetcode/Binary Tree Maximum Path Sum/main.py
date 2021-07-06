# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = None
        self.mps(root)
        return self.max

    def mps(self, root):
        if not root:
            return None

        left = self.mps(root.left)
        right = self.mps(root.right)

        if self.max is None:
            self.max = root.val

        self.max = max(self.max, root.val)

        if left:
            self.max = max(self.max, root.val + left)

        if right:
            self.max = max(self.max, root.val + right)

        if left and right:
            self.max = max(self.max, root.val + right + left)

        left_sum = left or 0
        right_sum = right or 0
        return max(root.val, root.val + left_sum, root.val + right_sum)
