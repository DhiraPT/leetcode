class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted([int(t[:2]) * 60 + int(t[3:]) for t in timePoints])
        min_difference = 720
        for i in range(1, len(timePoints)):
            min_difference = min(min_difference, timePoints[i] - timePoints[i-1])
        min_difference = min(min_difference, timePoints[0] + 1440 - timePoints[-1])
        return min_difference