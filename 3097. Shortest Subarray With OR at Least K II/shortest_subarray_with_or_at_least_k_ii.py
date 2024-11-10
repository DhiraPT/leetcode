class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1

        left = right = 0
        curr_or = 0
        bit_counts = [0] * 32
        min_length = float('inf')

        while right < len(nums):
            curr_or |= nums[right]

            for i in range(32):
                if nums[right] & (1 << i):
                    bit_counts[i] += 1

            while curr_or >= k:
                min_length = min(min_length, right - left + 1)
                for i in range(32):
                    if nums[left] & (1 << i):
                        bit_counts[i] -= 1
                        if bit_counts[i] == 0:
                            curr_or &= ~(1 << i)
                left += 1

            right += 1

        return -1 if min_length == float('inf') else min_length