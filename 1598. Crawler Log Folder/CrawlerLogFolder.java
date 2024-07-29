class Solution {
    public int minOperations(String[] logs) {
        int steps = 0;
        for (String op : logs) {
            if (op.equals("../")) {
                steps = Math.max(0, steps - 1);
            } else if (op.equals("./")) {
                continue;
            } else if (op.endsWith("/")) {
                steps += 1;
            }
        }
        return steps;
    }
}
