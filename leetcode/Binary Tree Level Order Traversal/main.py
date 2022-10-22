from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        frontier = deque([(root, 0)]) if root else []

        while frontier:
            current, level = frontier.popleft()
            print(f"current: {current.val}")

            if current.left:
                frontier.append((current.left, level + 1))

            if current.right:
                frontier.append((current.right, level + 1))

            try:
                print(f"appending {current.val} to result: {result}")
                result[level].append(current.val)
            except IndexError:
                print(f"level: {level} not in result, adding level")
                result.append([current.val])

            print(f"result list updated: {result}")

        return result

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Slightly simplified version
        """
        result = []
        if root is None:
            return result

        frontier = deque([(root, 0)])
        while frontier:
            current, level = frontier.popleft()
            try:
                result[level].append(current.val)
            except IndexError:
                result.append([current.val])

            if current.left:
                frontier.append((current.left, level + 1))

            if current.right:
                frontier.append((current.right, level + 1))

        return result
