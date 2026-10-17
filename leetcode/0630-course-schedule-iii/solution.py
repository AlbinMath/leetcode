import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        total, h = 0, []
        for d, end in courses:
            total += d
            heapq.heappush(h, -d)
            if total > end:
                total += heapq.heappop(h)
        return len(h)
