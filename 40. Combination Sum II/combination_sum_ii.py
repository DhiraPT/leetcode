class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [c for c in candidates if c <= target]

        candidates.sort()

        dp = [set() for _ in range(target+1)]
        dp[0].add(())

        for c in candidates:
            for j in range(target - c, -1, -1):
                for res in dp[j]:
                    dp[j+c].add(res + (c,))

        return dp[target]