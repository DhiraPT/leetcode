class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_nums(prefix):
            count = 0
            first = last = prefix
            while first <= n:
                count += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return count

        i = 1
        k -= 1

        while k > 0:
            count = count_nums(i)
            if count <= k:
                i += 1
                k -= count
            else:
                i *= 10
                k -= 1
        return i