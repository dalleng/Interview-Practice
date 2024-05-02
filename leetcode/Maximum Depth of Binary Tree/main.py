class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return (
            max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
            if root
            else 0
        )
