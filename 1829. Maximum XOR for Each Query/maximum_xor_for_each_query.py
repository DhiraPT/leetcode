class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        curr_xor = 0
        res = [0] * n
        mask = (1 << maximumBit) - 1

        for i, num in enumerate(nums):
            curr_xor ^= num
            res[n-i-1] = curr_xor ^ mask

        return res