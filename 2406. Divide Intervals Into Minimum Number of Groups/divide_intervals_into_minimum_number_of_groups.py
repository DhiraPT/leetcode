class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []

        for left, right in intervals:
            events.append((left, 1))
            events.append((right + 1, -1))

        events.sort()

        max_count = 0
        curr_count = 0
        for event in events:
            curr_count += event[1]
            max_count = max(max_count, curr_count)

        return max_count