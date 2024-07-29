class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        Map<Integer, Integer> f = new HashMap<>();
        int maxLen = 0;
        int l = 0;
        for (int r = 0; r < nums.length; r++) {
            f.put(nums[r], f.getOrDefault(nums[r], 0) + 1);
            while (f.get(nums[r]) > k) {
                f.put(nums[l], f.get(nums[l]) - 1);
                if (f.get(nums[l]) == 0) {
                    f.remove(nums[l]);
                }
                l++;
            }
            maxLen = Math.max(maxLen, r-l+1);
        }
        return maxLen;
    }
}
