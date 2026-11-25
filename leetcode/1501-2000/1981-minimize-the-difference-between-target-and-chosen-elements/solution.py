class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sums = {0}
        for row in mat:
            vals = set(row)
            nxt = set()
            over = float('inf')
            for s in sums:
                for v in vals:
                    t = s + v
                    if t < target:
                        nxt.add(t)
                    else:
                        over = min(over, t)
            if over != float('inf'):
                nxt.add(over)
            sums = nxt
        return min(abs(s - target) for s in sums)
