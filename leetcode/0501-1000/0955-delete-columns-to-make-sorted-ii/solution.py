class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        settled = [False] * (n - 1)
        deletions = 0

        for c in range(m):
            # does this column violate order for any unsettled pair?
            if any(not settled[i] and strs[i][c] > strs[i + 1][c] for i in range(n - 1)):
                deletions += 1
                continue

            # keep it: settle pairs that are now strictly ordered
            for i in range(n - 1):
                if strs[i][c] < strs[i + 1][c]:
                    settled[i] = True

        return deletions
