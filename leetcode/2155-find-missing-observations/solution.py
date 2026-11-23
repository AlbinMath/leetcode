class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missing = mean * (n + m) - sum(rolls)
        if missing < n or missing > 6 * n:
            return []
        q, r = divmod(missing, n)
        return [q + 1] * r + [q] * (n - r)
