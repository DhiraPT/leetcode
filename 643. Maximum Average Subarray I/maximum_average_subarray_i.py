class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)

        max_sum = curr_sum = sum(nums[:k])

        for i in range(1, len(nums)-k+1):
            curr_sum = curr_sum - nums[i-1] + nums[i+k-1]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k