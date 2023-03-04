/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> output = new ArrayList<>();
        
        if (root == null) return output;
        Stack <TreeNode> stack = new Stack<>();
        stack.add(root);
        
        while (!stack.isEmpty()) {
            TreeNode current_node = stack.pop();
            output.add(0, current_node.val);
            
            if (current_node.left != null)
                stack.add(current_node.left);
            if (current_node.right != null)
                stack.add(current_node.right);
        }
        
        return output;
    }
}