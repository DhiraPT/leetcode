class Solution:
    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        curr_sum = 0
        q = deque()
        shortest_length = float('inf')

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum >= target_sum and i + 1 < shortest_length:
                shortest_length = i + 1

            while q and curr_sum - q[0][0] >= target_sum:
                _, j = q.popleft()
                shortest_length = min(shortest_length, i - j)

            while q and q[-1][0] > curr_sum:
                q.pop()

            q.append((curr_sum, i))

        return -1 if shortest_length == float('inf') else shortest_length