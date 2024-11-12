class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        max_beauty = 0
        for i in items:
            max_beauty = max(max_beauty, i[1])
            i[1] = max_beauty

        ans = []

        for q in queries:
            index = bisect.bisect_right(items, [q, float('inf')]) - 1
            if index >= 0:
                ans.append(items[index][1])
            else:
                ans.append(0)

        return ans