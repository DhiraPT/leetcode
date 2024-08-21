class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                sums.append(curr_sum)
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)