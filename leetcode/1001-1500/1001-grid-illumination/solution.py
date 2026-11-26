
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        active_lamps = set()
        rows = defaultdict(int)
        cols = defaultdict(int)
        diag1 = defaultdict(int) 
        diag2 = defaultdict(int)
        for r, c in lamps:
            if (r, c) not in active_lamps:
                active_lamps.add((r, c))
                rows[r] += 1
                cols[c] += 1
                diag1[r - c] += 1
                diag2[r + c] += 1     
        ans = []
        for qr, qc in queries:
            if rows[qr] > 0 or cols[qc] > 0 or diag1[qr - qc] > 0 or diag2[qr + qc] > 0:
                ans.append(1)
            else:
                ans.append(0)
            for nr in (qr - 1, qr, qr + 1):
                for nc in (qc - 1, qc, qc + 1):
                    if (nr, nc) in active_lamps:
                        active_lamps.remove((nr, nc))
                        rows[nr] -= 1
                        cols[nc] -= 1
                        diag1[nr - nc] -= 1
                        diag2[nr + nc] -= 1 
        return ans
