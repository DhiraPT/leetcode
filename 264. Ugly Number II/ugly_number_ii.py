class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_heap = []
        heapq.heappush(ugly_heap, 1)
        visited = set([1])

        while n > 0:
            curr_ugly = heapq.heappop(ugly_heap)
            n -= 1

            if curr_ugly * 2 not in visited:
                heapq.heappush(ugly_heap, curr_ugly * 2)
                visited.add(curr_ugly * 2)
            if curr_ugly * 3 not in visited:
                heapq.heappush(ugly_heap, curr_ugly * 3)
                visited.add(curr_ugly * 3)
            if curr_ugly * 5 not in visited:
                heapq.heappush(ugly_heap, curr_ugly * 5)
                visited.add(curr_ugly * 5)

        return curr_ugly