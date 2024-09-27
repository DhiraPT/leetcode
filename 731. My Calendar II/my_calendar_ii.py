class MyCalendarTwo:

    def __init__(self):
        self.timeline = []

    def book(self, start: int, end: int) -> bool:
        temp_timeline = self.timeline + [(start, 1), (end, -1)]

        temp_timeline.sort()

        ongoing_events = 0

        for time, event in temp_timeline:
            ongoing_events += event
            if ongoing_events >= 3:
                return False

        self.timeline = temp_timeline
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)