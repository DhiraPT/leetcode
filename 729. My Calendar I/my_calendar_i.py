class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_right(self.bookings, (start, end))
        if i > 0 and self.bookings[i-1][1] > start:
            return False
        if i < len(self.bookings) and end > self.bookings[i][0]:
            return False
        self.bookings.insert(i, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)