class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        lis_len = [1] * n
        lis = [nums[0]]

        for i in range(1, n):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
                lis_len[i] = len(lis)
            else:
                index = bisect.bisect_left(lis, nums[i])
                lis[index] = nums[i]
                lis_len[i] = index + 1

        lds_len = [1] * n
        lds = [nums[-1]]

        for i in range(n - 2, -1, -1):
            if nums[i] > lds[-1]:
                lds.append(nums[i])
                lds_len[i] = len(lds)
            else:
                index = bisect.bisect_left(lds, nums[i])
                lds[index] = nums[i]
                lds_len[i] = index + 1

        max_mountain_length = 0
        for i in range(1, n - 1):
            if lis_len[i] > 1 and lds_len[i] > 1:
                max_mountain_length = max(max_mountain_length, lis_len[i] + lds_len[i] - 1)

        return n - max_mountain_length