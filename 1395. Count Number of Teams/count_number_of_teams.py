class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        for i in range(1, n-1):
            less_left = more_left = less_right = more_right = 0

            for j in range(i):
                if rating[j] < rating[i]:
                    less_left += 1
                elif rating[j] > rating[i]:
                    more_left += 1

            for r in range(i+1, n):
                if rating[r] > rating[i]:
                    more_right += 1
                elif rating[r] < rating[i]:
                    less_right += 1
            teams += less_left * more_right + more_left * less_right

        return teams
