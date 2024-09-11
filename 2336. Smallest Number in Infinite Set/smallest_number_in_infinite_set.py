class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.nums = set()
        self.smallest = 1  # Smallest number that has not been popped

    def popSmallest(self) -> int:
        if not self.heap:
            val = self.smallest
            self.smallest += 1
            return val
        val = heapq.heappop(self.heap)
        self.nums.remove(val)
        return val

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.nums:
            heapq.heappush(self.heap, num)
            self.nums.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)