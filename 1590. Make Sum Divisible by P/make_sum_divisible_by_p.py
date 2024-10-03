class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        excess_modulo = total_sum % p

        if excess_modulo == 0:
            return 0

        prefix_modulos = {0: -1}
        min_length = len(nums)
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            curr_modulo = curr_sum % p
            remove_modulo = (curr_modulo - excess_modulo) % p

            if remove_modulo in prefix_modulos:
                min_length = min(min_length, i - prefix_modulos[remove_modulo])

            prefix_modulos[curr_modulo] = i

        return min_length if min_length != len(nums) else -1