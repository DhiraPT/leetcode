class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            num2: int = target - num
            if num2 in dic:
                return [dic[num2], i]
            dic[num] = i