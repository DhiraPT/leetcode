class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        empty = 0
        while numBottles > 0:
            count += numBottles
            newEmpty = numBottles + empty
            numBottles = newEmpty // numExchange
            empty = newEmpty % numExchange
        return count
