class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> sums(n);
        if (k == 0) {
            return sums;
        }

        int curr_sum = 0, left = 1, right = 1;
        while (right - left < std::abs(k)) {
            curr_sum += code[right%n];
            right++;
        }

        if (k > 0) {
            sums[0] = curr_sum;
            while (left < n) {
                curr_sum += code[right%n] - code[left%n];
                sums[left] = curr_sum;
                ++right;
                ++left;
            }
        } else if (k < 0) {
            sums[-k] = curr_sum;
            while (left <= n) {
                curr_sum += code[right%n] - code[left%n];
                ++right;
                ++left;
                sums[right%n] = curr_sum;
            }
        }

        return sums;
    }
};