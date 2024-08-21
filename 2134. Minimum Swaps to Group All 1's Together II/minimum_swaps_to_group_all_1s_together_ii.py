class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        count_ones = nums.count(1)
        nums2 = nums + nums
        count = nums2[:count_ones].count(1)
        max_count = count

        for i in range(1, len(nums)):
            if nums2[i+count_ones-1] == 1:
                count += 1
            if nums2[i-1] == 1:
                count -= 1
            max_count = max(max_count, count)

        return count_ones - max_count