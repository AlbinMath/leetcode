class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = [0] * 26
        l = 0
        ans = 0
        for ch in s:
            c = ord(ch) - 97
            cnt[c] += 1
            while cnt[c] >= k:
                cnt[ord(s[l]) - 97] -= 1
                l += 1
            ans += l
        return ans
