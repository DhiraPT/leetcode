class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        std::unordered_map<int, int> counts;
        int left = 0, right = 0;
        long long max_sum = 0, curr_sum = 0;

        while (right < nums.size()) {
            curr_sum += nums[right];
            counts[nums[right++]]++;
            if (right - left >= k) {
                if (counts.size() == k && curr_sum > max_sum) {
                    max_sum = curr_sum;
                }
                curr_sum -= nums[left];
                counts[nums[left]]--;
                if (counts[nums[left]] == 0) {
                    counts.erase(nums[left]);
                }
                ++left;
            }
        }

        return max_sum;
    }
};