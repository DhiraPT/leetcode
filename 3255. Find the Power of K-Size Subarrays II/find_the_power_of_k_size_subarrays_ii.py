class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        n = len(nums)
        res = []

        i = 0
        prev_valid = False
        while i <= n - k:
            if prev_valid:
                if nums[i+k-1] - nums[i+k-2] == 1:
                    res.append(nums[i+k-1])
                else:
                    res.append(-1)
                    prev_valid = False
                i += 1
            else:
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
                prev_valid = is_valid

        return res