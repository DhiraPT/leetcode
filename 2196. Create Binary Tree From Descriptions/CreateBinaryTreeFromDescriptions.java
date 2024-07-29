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
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> valNodeMap = new HashMap<>(10001);
        Set<Integer> children = new HashSet<>(10000);

        for (int[] desc : descriptions) {
            int p = desc[0];
            int c = desc[1];
            int isLeft = desc[2];
            valNodeMap.putIfAbsent(p, new TreeNode(p));
            valNodeMap.putIfAbsent(c, new TreeNode(c));
            if (isLeft == 1) {
                valNodeMap.get(p).left = valNodeMap.get(c);
            } else if (isLeft == 0) {
                valNodeMap.get(p).right = valNodeMap.get(c);
            }
            children.add(c);
        }

        for (int val : valNodeMap.keySet()) {
            if (!children.contains(val)) {
                return valNodeMap.get(val);
            }
        }

        return null;
    }
}
