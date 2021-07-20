# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        frontier = deque([(root, 0)]) if root else None
        result = []

        while frontier:
            current, level = frontier.popleft()
            if current.left:
                frontier.append((current.left, level + 1))

            if current.right:
                frontier.append((current.right, level + 1))

            if level % 2 == 0:
                try:
                    result[level].append(current.val)
                except IndexError:
                    result.append([current.val])
            else:
                try:
                    result[level] = [current.val] + result[level]
                except IndexError:
                    result.append([current.val])

        return result
