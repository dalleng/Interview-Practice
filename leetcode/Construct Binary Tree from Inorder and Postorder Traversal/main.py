import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def node_with_children(cls, val, left, right):
        node = cls(val)
        node.left = left
        node.right = right
        return node

    def inorder(self):
        inorder_list = []

        def _inorder(root):
            if not root:
                return
            else:
                _inorder(root.left)
                inorder_list.append(root)
                _inorder(root.right)

        _inorder(self)
        return inorder_list

    def postorder(self):
        postorder_list = []

        def _postorder(root):
            if not root:
                return
            else:
                _postorder(root.left)
                _postorder(root.right)
                postorder_list.append(root)

        _postorder(self)
        return postorder_list


class TraversalsTest(unittest.TestCase):
    def test_single_node(self):
        self.assertEquals([node.val for node in TreeNode(1).inorder()], [1])
        self.assertEquals([node.val for node in TreeNode(1).postorder()], [1])

    def test_full_tree(self):
        """
        All non-leaves nodes have both left and right childs

        Image:
        http://flylib.com/books/2/264/1/html/2/images/fig21-11.jpg
        """
        node_e = TreeNode.node_with_children("E", TreeNode("H"), TreeNode("I"))
        node_c = TreeNode.node_with_children("C", TreeNode("F"), TreeNode("G"))
        node_b = TreeNode.node_with_children("B", TreeNode("D"), node_e)
        node_a = TreeNode.node_with_children("A", node_b, node_c)
        self.assertEquals([node.val for node in node_a.inorder()], list("DBHEIAFCG"))
        self.assertEquals([node.val for node in node_a.postorder()], list("DHIEBFGCA"))

    def test_single_child(self):
        """
        Some non-leaves nodes have only a single child

        Image:
        http://3.bp.blogspot.com/-BVjfxybgcBs/Uf1xKT9bZsI/AAAAAAAAAYA/9aDf1P4819U/s1600/btreeTrav2.gif
        """
        node_h = TreeNode.node_with_children("H", TreeNode("G"), None)
        node_f = TreeNode.node_with_children("F", TreeNode("B"), node_h)
        node_t = TreeNode.node_with_children("T", None, TreeNode("W"))
        node_y = TreeNode.node_with_children("Y", node_t, TreeNode("Z"))
        node_s = TreeNode.node_with_children("S", TreeNode("R"), node_y)
        node_p = TreeNode.node_with_children("P", node_f, node_s)
        self.assertEquals([node.val for node in node_p.inorder()], list("BFGHPRSTWYZ"))
        self.assertEquals(
            [node.val for node in node_p.postorder()], list("BGHFRWTZYSP")
        )

    def test_unbalanced(self):
        """
                3
              /
            2
          /
        1
        """
        left = TreeNode.node_with_children(2, TreeNode(1), None)
        root = TreeNode.node_with_children(3, left, None)
        self.assertEquals([node.val for node in root.inorder()], [1, 2, 3])
        self.assertEquals([node.val for node in root.postorder()], [1, 2, 3])


class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        if len(inorder) == 1:
            return TreeNode(postorder.pop())
        else:
            root = postorder.pop()
            i = inorder.index(root)

            inorderLeft = inorder[:i]
            inorderRight = inorder[i + 1 :]

            root = TreeNode(root)
            root.right = self.buildTree(inorderRight, postorder)
            root.left = self.buildTree(inorderLeft, postorder)

            return root


class BuildTreeTest(unittest.TestCase):
    def test_full_tree(self):
        root = Solution().buildTree(list("DBHEIAFCG"), list("DHIEBFGCA"))
        self.assertEquals([node.val for node in root.inorder()], list("DBHEIAFCG"))
        self.assertEquals([node.val for node in root.inorder()], list("DBHEIAFCG"))

    def test_single_child(self):
        root = Solution().buildTree(list("BFGHPRSTWYZ"), list("BGHFRWTZYSP"))
        self.assertEquals([node.val for node in root.inorder()], list("BFGHPRSTWYZ"))
        self.assertEquals([node.val for node in root.postorder()], list("BGHFRWTZYSP"))


if __name__ == "__main__":
    unittest.main()
