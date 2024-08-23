class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        l = 0
        r = len(nums) - 1

        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum > k:
                r -= 1
            elif curr_sum < k:
                l += 1
            else:
                count += 1
                r -= 1
                l += 1

        return count