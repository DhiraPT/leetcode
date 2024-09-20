class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def compute_ways(i, j):
            if i == j:
                return [elements[i]]

            res = []
            for k in range(i+1, j, 2):
                left = compute_ways(i, k-1)
                right = compute_ways(k+1, j)
                op = elements[k]

                for l in left:
                    for r in right:
                        if op == '+':
                            res.append(l + r)
                        elif op == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
            return res

        elements = []
        num = ''
        for c in expression:
            if c in '+-*':
                elements.append(int(num))
                elements.append(c)
                num = ''
            else:
                num += c
        elements.append(int(num))

        return compute_ways(0, len(elements)-1)