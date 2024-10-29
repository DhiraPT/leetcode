class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending = 0
        res = float('-inf')

        for num in nums:
            max_ending += num
            res = max(res, max_ending)
            if max_ending < 0:
                max_ending = 0

        return res