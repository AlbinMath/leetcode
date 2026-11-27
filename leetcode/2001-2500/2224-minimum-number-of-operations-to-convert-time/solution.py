class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def to_min(t: str) -> int:
            h, m = t.split(':')
            return int(h) * 60 + int(m)

        diff = to_min(correct) - to_min(current)
        ops = 0
        for step in (60, 15, 5, 1):
            ops += diff // step
            diff %= step
        return ops
