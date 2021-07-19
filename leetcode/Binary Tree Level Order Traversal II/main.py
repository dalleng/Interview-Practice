from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = deque()
        r_level = None
        frontier = deque([(root, 0)] if root else [])

        while frontier:
            current, level = frontier.popleft()
            if current.left:
                frontier.append((current.left, level + 1))

            if current.right:
                frontier.append((current.right, level + 1))

            if r_level is None or level > r_level:
                r_level = level
                result.appendleft([current.val])
            else:
                result[0].append(current.val)

        return result
