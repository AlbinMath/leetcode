
class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        merged = []
        added = False

        for start, end in self.ranges:
            if end < left:
                merged.append((start, end))
            elif start > right:
                if not added:
                    merged.append((left, right))
                    added = True
                merged.append((start, end))
            else:
                left = min(left, start)
                right = max(right, end)

        if not added:
            merged.append((left, right))

        self.ranges = merged

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.ranges:
            if start <= left and right <= end:
                return True
            if start > left:
                break
        return False

    def removeRange(self, left: int, right: int) -> None:
        remaining = []

        for start, end in self.ranges:
            if end <= left or start >= right:
                remaining.append((start, end))
            else:
                if start < left:
                    remaining.append((start, left))
                if end > right:
                    remaining.append((right, end))

        self.ranges = remaining

