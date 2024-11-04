class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s2 = s + s
        return goal in s2 and len(goal) == len(s)