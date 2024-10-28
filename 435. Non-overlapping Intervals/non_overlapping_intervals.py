class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        end, count = float('-inf'), 0

        for i in intervals:
            if i[0] < end:
                continue
            count += 1
            end = i[1]

        return len(intervals) - count