class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_num = -100_000
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num[0], 0, i))
            max_num = max(max_num, num[0])

        min_range = max_num - min_heap[0][0]
        range_tuple = (max_num, min_heap[0][0])
        while True:
            _, i, nums_i = heapq.heappop(min_heap)
            if i == len(nums[nums_i]) - 1:
                break
            i += 1
            heapq.heappush(min_heap, (nums[nums_i][i], i, nums_i))
            max_num = max(max_num, nums[nums_i][i])
            if max_num - min_heap[0][0] < min_range:
                min_range = max_num - min_heap[0][0]
                range_tuple = (max_num, min_heap[0][0])

        return range_tuple