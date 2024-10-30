class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                low, high = 0, len(ans) - 1
                while low <= high:
                    mid = (low + high) >> 1
                    if nums[i] > ans[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                ans[low] = nums[i]

        return len(ans)