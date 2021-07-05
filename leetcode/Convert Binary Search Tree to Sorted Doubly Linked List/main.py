# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.head = root
        self.traverse(root)

        if self.head:
            current = self.head
            while current.right:
                current = current.right

            self.head.left = current
            current.right = self.head

        return self.head

    def traverse(self, root):
        if not root:
            return

        if root.val < self.head.val:
            self.head = root

        if not root.left and not root.right:
            return (root, root)

        left = self.traverse(root.left)
        right = self.traverse(root.right)

        if left:
            min_l, max_l = left
            root.left = max_l
            max_l.right = root
        else:
            min_l = root

        if right:
            min_r, max_r = right
            root.right = min_r
            min_r.left = root
        else:
            max_r = root

        return (min_l, max_r)
