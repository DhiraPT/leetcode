class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0
        for i in range(24):
            curr_count = 0
            for num in candidates:
                if (num >> i) & 1 != 0:
                    curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
        return max_count