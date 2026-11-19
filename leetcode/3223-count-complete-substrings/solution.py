class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def count_segment(seg: str) -> int:
            m = len(seg)
            res = 0
            for d in range(1, 27):
                w = d * k
                if w > m:
                    break
                cnt = [0] * 26
                good = 0  # letters with count exactly k
                for i in range(m):
                    c = ord(seg[i]) - 97
                    cnt[c] += 1
                    if cnt[c] == k:
                        good += 1
                    elif cnt[c] == k + 1:
                        good -= 1
                    if i >= w:
                        o = ord(seg[i - w]) - 97
                        if cnt[o] == k:
                            good -= 1
                        elif cnt[o] == k + 1:
                            good += 1
                        cnt[o] -= 1
                    if i >= w - 1 and good == d:
                        res += 1
            return res

        ans = 0
        start = 0
        for i in range(1, n + 1):
            if i == n or abs(ord(word[i]) - ord(word[i - 1])) > 2:
                ans += count_segment(word[start:i])
                start = i
        return ans
