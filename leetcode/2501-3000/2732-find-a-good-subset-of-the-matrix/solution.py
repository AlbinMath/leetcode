class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        first = {}
        for i, row in enumerate(grid):
            mask = 0
            for j, v in enumerate(row):
                if v:
                    mask |= 1 << j
            if mask == 0:
                return [i]
            if mask not in first:
                first[mask] = i

        masks = list(first.items())
        for a, i in masks:
            for b, j in masks:
                if a & b == 0 and i != j:
                    return sorted([i, j])
        return []
