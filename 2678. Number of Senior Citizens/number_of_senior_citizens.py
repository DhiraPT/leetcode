class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for p in details:
            if int(p[11:13]) > 60:
                count += 1
        return count