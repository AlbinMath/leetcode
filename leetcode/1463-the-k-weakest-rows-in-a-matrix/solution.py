class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        strengths = []

        for i, row in enumerate(mat):
            soldiers = sum(row)
            strengths.append((soldiers, i))

        strengths.sort()

        return [index for soldiers, index in strengths[:k]]
