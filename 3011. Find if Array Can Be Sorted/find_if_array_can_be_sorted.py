class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        num_bits = [num.bit_count() for num in nums]
        prev_max, prev_bits, curr_max, curr_bits = 0, 0, nums[0], num_bits[0]

        for i, num in enumerate(nums):
            if num_bits[i] != curr_bits:
                prev_max, prev_bits, curr_max, curr_bits = curr_max, curr_bits, num, num_bits[i]
            if num < prev_max:
                return False
            if num > curr_max:
                curr_max = num

        return True