/**
 * Minimum Depth of Binary Tree
 * https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
 *
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.ArrayDeque;
import java.util.AbstractMap.SimpleEntry;
 
public class Solution {
    public int minDepth(TreeNode root) {
        int depth = 0;
        
        if (root != null) {
            ArrayDeque<SimpleEntry<TreeNode, Integer>> frontier = new ArrayDeque<SimpleEntry<TreeNode, Integer>>();
            frontier.add(new SimpleEntry<TreeNode, Integer>(root, 1));
        
            while (!frontier.isEmpty()) {
                SimpleEntry<TreeNode, Integer> current = frontier.poll();
                if (current.getKey().right == null && current.getKey().left == null) {
                    depth = current.getValue();
                    break;
                } else {
                    if (current.getKey().right != null) {
                        frontier.add(new SimpleEntry<TreeNode, Integer>(current.getKey().right, current.getValue() + 1));
                    }
                    
                    if (current.getKey().left != null) {
                        frontier.add(new SimpleEntry<TreeNode, Integer>(current.getKey().left, current.getValue() + 1));
                    }
                }
            }
        }
        
        return depth;
    }
}
