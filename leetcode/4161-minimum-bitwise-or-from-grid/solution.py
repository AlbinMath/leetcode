class Solution(object):
    def minimumOR(self, grid):
        ans = (1 << 17) - 1
        for b in range(16, -1, -1):
            cand = ans ^ (1 << b)
            ok = True
            for row in grid:
                found = False
                for x in row:
                    if x | cand == cand:
                        found = True
                        break
                if not found:
                    ok = False
                    break
            if ok:
                ans = cand
        return ans
