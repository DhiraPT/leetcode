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
    public String getDirections(TreeNode root, int startValue, int destValue) {
        StringBuilder pathToS = findPath(root, startValue).reverse();
        StringBuilder pathToT = findPath(root, destValue).reverse();

        int i = 0;
        while (i < pathToS.length() && i < pathToT.length() && pathToS.charAt(i) == pathToT.charAt(i)) {
            i++;
        }

        StringBuilder resPath = new StringBuilder();
        for (int j = i; j < pathToS.length(); j++) {
            resPath.append('U');
        }
        resPath.append(pathToT.substring(i));

        return resPath.toString();
    }

    StringBuilder findPath(TreeNode from, int value) {
        if (from == null) {
            return null;
        }

        if (from.val == value) {
            return new StringBuilder();
        }

        StringBuilder leftPath = findPath(from.left, value);
        if (leftPath != null) {
            return leftPath.append('L');
        }

        StringBuilder rightPath = findPath(from.right, value);
        if (rightPath != null) {
            return rightPath.append('R');
        }

        return null;
    }
}
