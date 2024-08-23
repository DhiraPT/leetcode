class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        i = 0
        while i <= n - k:
            is_valid = True
            for j in range(i, i + k - 1):
                if nums[j+1] - nums[j] != 1:
                    is_valid = False
                    break

            if is_valid:
                res.append(nums[i+k-1])
                i += 1
            else:
                res.extend([-1] * (min(n - k, j) + 1 - i))
                i = j + 1

        return res