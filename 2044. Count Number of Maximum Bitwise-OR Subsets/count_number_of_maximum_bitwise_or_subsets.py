class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        dp = [0] * (1 << int(math.log2(max(nums))) + 1)
        dp[0] = 1

        for num in nums:
            for i in range(max_or, -1, -1):
                dp[i|num] += dp[i]
            max_or |= num

        return dp[max_or]