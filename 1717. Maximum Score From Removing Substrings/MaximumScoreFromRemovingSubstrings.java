class Solution {
    public int maximumGain(String s, int x, int y) {
        int score;
        if (x > y) {
            score = processString(s, 'a', 'b', x, y);
        } else {
            score = processString(s, 'b', 'a', y, x);
        }
        return score;
    }

    private int processString(String s, char first, char second, int point1, int point2) {
        Stack<Character> stack = new Stack<>();
        int score = 0;
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == first && c == second) {
                stack.pop();
                score += point1;
            } else {
                stack.push(c);
            }
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        s = sb.reverse().toString();
        stack.clear();
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == second && c == first) {
                stack.pop();
                score += point2;
            } else {
                stack.push(c);
            }
        }
        return score;
    }
}
