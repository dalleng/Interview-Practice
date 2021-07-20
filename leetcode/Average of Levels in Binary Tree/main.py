# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        frontier = deque([(root, 0)]) if root else None

        while frontier:
            current, level = frontier.popleft()

            if current.left:
                frontier.append((current.left, level + 1))

            if current.right:
                frontier.append((current.right, level + 1))

            try:
                total, n = result[level]
                result[level] = (total + current.val, n + 1)
            except IndexError:
                result.append((current.val, 1))

        return [total / n for total, n in result]
