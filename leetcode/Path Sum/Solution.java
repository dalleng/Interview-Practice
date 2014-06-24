/**
 * Path Sum
 * https://oj.leetcode.com/problems/path-sum/
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
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        
        if (root.left == null && root.right == null) {
            return (sum - root.val) == 0;
        } else {
            boolean hasPathSum = hasPathSum(root.left, sum - root.val);
            
            if (!hasPathSum) {
                hasPathSum = hasPathSum(root.right, sum - root.val);
            }
            
            return hasPathSum;
        }
    }
}
