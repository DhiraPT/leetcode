class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]

        for p in prices[1:]:
            if buy_price < p:
                max_profit = max(max_profit, p - buy_price)
            else:
                buy_price = p

        return max_profit