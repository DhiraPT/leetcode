class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []

        for i in range(len(target)):
            if i == 0:
                if target[i] > 1:
                    res.extend(['Push', 'Pop'] * (target[i] - 1))
            else:
                res.extend(['Push', 'Pop'] * (target[i] - target[i-1] - 1))
            res.append('Push')

        return res
