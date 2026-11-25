class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        counts = [sum(row) for row in mat]
        best = max(counts)
        return [counts.index(best), best]
