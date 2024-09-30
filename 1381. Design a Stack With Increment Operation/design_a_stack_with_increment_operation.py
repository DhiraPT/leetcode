class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increment_values = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        index = len(self.stack) - 1
        val = self.increment_values[index]
        if index > 0:
            self.increment_values[index-1] += val
        self.increment_values[index] = 0

        return self.stack.pop() + val

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        self.increment_values[min(k, len(self.stack)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)