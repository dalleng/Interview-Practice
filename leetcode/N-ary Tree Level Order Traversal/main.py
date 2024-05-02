# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        result = []
        frontier = deque([(root, 0)]) if root else deque()

        while frontier:
            current, level = frontier.popleft()
            for child in current.children:
                frontier.append((child, level + 1))
            try:
                result[level].append(current.val)
            except IndexError:
                result.append([current.val])

        return result
