class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_i = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != zero_i:
                    nums[i], nums[zero_i] = nums[zero_i], nums[i]
                zero_i += 1