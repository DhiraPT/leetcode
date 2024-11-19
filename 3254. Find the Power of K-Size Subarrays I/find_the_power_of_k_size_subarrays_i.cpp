class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        if (k == 1) {
            return nums;
        }

        vector<int> powers(nums.size() - k + 1, -1);
        int length = 1;
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] + 1 == nums[i+1]) {
                ++length;
            } else {
                length = 1;
            }

            if (length >= k) {
                powers[i-k+2] = nums[i+1];
            }
        }

        return powers;
    }
};