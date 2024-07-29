class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []
        while nums:
            result.append(heapq.heappop(nums))
        return result
