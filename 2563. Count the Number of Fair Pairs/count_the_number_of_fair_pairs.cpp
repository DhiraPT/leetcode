class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        std::sort(nums.begin(), nums.end());
        long long count = 0;

        for (int i = 0; i < nums.size(); ++i) {
            auto smallest = std::lower_bound(nums.begin() + i + 1, nums.end(), lower - nums[i]);
            auto greatest = std::upper_bound(nums.begin() + i + 1, nums.end(), upper - nums[i]);
            count += greatest - smallest;
        }

        return count;
    }
};