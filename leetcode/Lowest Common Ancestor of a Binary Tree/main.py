# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = []
        path_q = []
        self.dfs(root, p, path_p)
        self.dfs(root, q, path_q)

        min_len = min(len(path_p), len(path_q))
        for i in range(-min_len, 0):
            if path_p[i] == path_q[i]:
                return path_p[i]

    def dfs(self, root, node, path):
        if not root:
            return False

        if root.val == node.val:
            path.append(root)
            return True

        left = self.dfs(root.left)
        if left:
            path.append(root)
            return True

        right = self.dfs(root.right)
        if right:
            path.append(root)
            return True

        return False
