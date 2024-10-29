class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []

        combinations = []

        def dfs(curr_combination, curr_sum, num):
            if len(curr_combination) == k:
                if curr_sum == n:
                    combinations.append(list(curr_combination))
                return

            for i in range(num, 10):
                if curr_sum + i > n:
                    break
                curr_combination.append(i)
                dfs(curr_combination, curr_sum + i, i + 1)
                curr_combination.pop()

        dfs([], 0, 1)

        return combinations