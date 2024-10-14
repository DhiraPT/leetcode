class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        score = 0
        while k > 0:
            num = -max_heap[0]
            score += num
            heapq.heapreplace(max_heap, -math.ceil(num / 3))
            k -= 1

        return score