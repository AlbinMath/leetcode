class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = [float(poured)]
        
        for r in range(query_row):
            next_row = [0.0] * (r + 2)
            for c in range(len(current_row)):
                overflow = (current_row[c] - 1.0) / 2.0
                if overflow > 0:
                    next_row[c] += overflow
                    next_row[c + 1] += overflow
            current_row = next_row
            
        return min(1.0, current_row[query_glass])
