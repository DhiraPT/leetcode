class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heappushpop(heap, num)

        return heap[0]