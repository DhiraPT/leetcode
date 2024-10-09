class Solution {
public:
    int minAddToMakeValid(string s) {
        stack<int> stack;
        int count = 0;
        for (auto &ch : s) {
            if (ch == '(') {
                stack.push(ch);
                count++;
            } else {
                if (!stack.empty()) {
                    stack.pop();
                    count--;
                } else {
                    count++;
                }
            }
        }
        return count;
    }
};