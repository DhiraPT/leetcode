class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(cmp))

        if nums[0] == '0':
            return '0'

        return ''.join(nums)