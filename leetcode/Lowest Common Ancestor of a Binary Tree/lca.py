# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        patha = self.dfs(root, p)
        print([n.val for n in patha])
        pathb = self.dfs(root, q)
        print([n.val for n in pathb])
        seen = set()
        while patha or pathb:
            for path in (patha, pathb):
                try:
                    n = path.pop()
                    if n in seen:
                        return n
                    else:
                        seen.add(n)
                except IndexError:
                    continue

    def dfs(self, root, goal):
        print("root:{} goal:{}".format(root.val, goal.val))
        frontier = [[root, False, False]]
        while frontier:
            node, seen_l, seen_r = frontier[-1]
            if node == goal:
                break
            elif seen_l and seen_r:
                frontier.pop()
            else:
                if not seen_l:
                    frontier[-1][1] = True
                    if node.left:
                        frontier.append([node.left, False, False])
                elif not seen_r:
                    frontier[-1][2] = True
                    if node.right:
                        frontier.append([node.right, False, False])
        return [node for node, sl, sr in frontier]
