class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0

        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)

        best = minutes[0] + 1440 - minutes[-1]  # wraparound gap
        for i in range(1, len(minutes)):
            best = min(best, minutes[i] - minutes[i - 1])
        return best
