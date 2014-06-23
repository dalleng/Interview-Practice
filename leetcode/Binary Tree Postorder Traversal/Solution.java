/**
 * Binary Tree Postorder Traversal 
 * https://oj.leetcode.com/problems/binary-tree-postorder-traversal/
 *
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> nodes = new ArrayList<Integer>();
        
        if (root != null) {
            if (root.left == null && root.right == null) {
                nodes.add(root.val);
            } else {
                nodes = postorderTraversal(root.left);
                nodes.addAll(postorderTraversal(root.right));
                nodes.add(root.val);
            }
        }
        
        return nodes;
    }
}
