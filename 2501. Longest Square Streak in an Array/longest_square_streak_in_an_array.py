class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        nums_set = set(nums)
        max_length = 0

        for num in nums:
            curr_length = 1
            for i in range(5):
                if num**2 in nums_set:
                    curr_length += 1
                    num **= 2
                else:
                    max_length = max(max_length, curr_length)
                    break

        return max_length if max_length >= 2 else -1