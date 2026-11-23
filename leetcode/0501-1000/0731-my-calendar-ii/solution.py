class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.overlaps:
            if startTime < e and endTime > s:
                return False

        for s, e in self.events:
            l, r = max(startTime, s), min(endTime, e)
            if l < r:
                self.overlaps.append((l, r))

        self.events.append((startTime, endTime))
        return True
