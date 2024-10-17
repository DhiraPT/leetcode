class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a, b = nums[0], max(nums[0], nums[1])
        c = b

        for i in range(2, len(nums)):
            c = max(a + nums[i], b)
            a, b = b, c

        return c