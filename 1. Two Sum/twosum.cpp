class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int num2 = target - nums[i];
            if (map.find(num2) != map.end()) {
                return {map[num2], i};
            }
            map.insert({nums[i], i});
        }
        return {};
    }
};