class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cnt = [0] * 26
            d = 0
            mx = 0
            for j in range(i, n):
                k = ord(s[j]) - 97
                if cnt[k] == 0:
                    d += 1
                cnt[k] += 1
                if cnt[k] > mx:
                    mx = cnt[k]
                length = j - i + 1
                if mx * d == length and length > ans:
                    ans = length
        return ans
