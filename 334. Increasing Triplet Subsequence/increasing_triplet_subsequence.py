class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        num_i = num_j = math.inf

        for num in nums:
            if num <= num_i:
                num_i = num
            elif num <= num_j:
                num_j = num
            else:
                return True

        return False