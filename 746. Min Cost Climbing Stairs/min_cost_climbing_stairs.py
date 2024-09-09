class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step2, step1 = 0, 0

        for i in range(2, len(cost)+1):
            curr_step =  min(step1 + cost[i-1], step2 + cost[i-2])
            step2, step1 = step1, curr_step

        return curr_step