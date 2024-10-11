class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for i, (arrival, leaving) in enumerate(times):
            events.append((arrival, 1, i))
            events.append((leaving, -1, i))
        events.sort()

        free_seats = list(range(len(times)))
        heapq.heapify(free_seats)
        seats_dict = {}

        for t, e, i in events:
            if e == 1:
                num = heapq.heappop(free_seats)
                if i == targetFriend:
                    return num
                seats_dict[i] = num
            else:
                heapq.heappush(free_seats, seats_dict[i])

        return -1