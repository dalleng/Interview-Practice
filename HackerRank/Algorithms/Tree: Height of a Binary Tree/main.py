class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def height(root):
    def dfs(root):
        return max(dfs(root.left) + 1, dfs(root.right) + 1) if root else 0
    return dfs(root) - 1 if root else 0
