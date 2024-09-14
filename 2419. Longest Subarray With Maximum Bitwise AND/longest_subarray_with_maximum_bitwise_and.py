class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        max_length = curr_length = 0

        for i in range(len(nums)):
            if nums[i] == max_and:
                curr_length += 1
                if i == len(nums) - 1:
                    max_length = max(max_length, curr_length)
            else:
                max_length = max(max_length, curr_length)
                curr_length = 0

        return max_length