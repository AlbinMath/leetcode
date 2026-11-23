class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        need = [0] * 26
        for ch in word2:
            need[ord(ch) - 97] += 1
        missing = sum(1 for x in need if x > 0)

        cnt = [0] * 26
        ans = 0
        r = 0  # window is [l, r)
        for l in range(n):
            while r < n and missing > 0:
                c = ord(word1[r]) - 97
                cnt[c] += 1
                if need[c] > 0 and cnt[c] == need[c]:
                    missing -= 1
                r += 1
            if missing == 0:
                ans += n - r + 1
            # remove word1[l]
            c = ord(word1[l]) - 97
            if need[c] > 0 and cnt[c] == need[c]:
                missing += 1
            cnt[c] -= 1
        return ans
