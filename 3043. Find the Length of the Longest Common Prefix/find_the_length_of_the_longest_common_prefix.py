class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr_1_prefixes = set()
        for num in arr1:
            while num > 0:
                arr_1_prefixes.add(num)
                num //= 10

        max_length = 0
        for num in arr2:
            while num > 0:
                if num in arr_1_prefixes:
                    max_length = max(max_length, int(math.log10(num)) + 1)
                    break
                num //= 10

        return max_length