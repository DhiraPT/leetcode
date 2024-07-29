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
    int res = 0;

    public int countPairs(TreeNode root, int distance) {
        dfs(root, distance);
        return res;
    }

    int[] dfs(TreeNode node, int distance) {
        int[] leafDistances = new int[distance+1];

        if (node == null) {
            return leafDistances;
        }

        if (node.left == null && node.right == null) {
            leafDistances[1] = 1;
            return leafDistances;
        }

        int[] leftDistances = dfs(node.left, distance);
        int[] rightDistances = dfs(node.right, distance);

        for (int l = 1; l < distance + 1; l++) {
            for (int r = 1; r < distance + 1; r++) {
                if (l + r <= distance) {
                    res += leftDistances[l] * rightDistances[r];
                }
            }
        }

        for (int i = 1; i < distance; i++) {
            leafDistances[i+1] = leftDistances[i] + rightDistances[i];
        }

        return leafDistances;
    }
}
