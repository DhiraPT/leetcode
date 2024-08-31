class RecentCounter:

    def __init__(self):
        self.counter = deque()

    def ping(self, t: int) -> int:
        while self.counter and self.counter[0] < t - 3000:
            self.counter.popleft()
        self.counter.append(t)
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)