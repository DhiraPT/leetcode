class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        end, non_overlapping = float('-inf'), 0

        for p in points:
            if p[0] <= end:
                continue
            non_overlapping += 1
            end = p[1]

        return non_overlapping