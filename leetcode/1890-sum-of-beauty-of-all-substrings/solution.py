class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0

        for i in range(n):
            cnt = [0] * 26
            for j in range(i, n):
                cnt[ord(s[j]) - 97] += 1
                present = [c for c in cnt if c]
                total += max(present) - min(present)

        return total
