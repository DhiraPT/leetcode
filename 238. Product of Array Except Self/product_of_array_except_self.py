class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        product = 1
        for i in range(n):
            res[i] *= product
            product *= nums[i]

        product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= product
            product *= nums[i]

        return res
