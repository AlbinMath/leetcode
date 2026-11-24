class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        def at_least(m: int) -> int:
            cnt = [0] * 5
            have = 0       # distinct vowels in window
            cons = 0       # consonants in window
            r = 0          # window is [l, r)
            res = 0
            for l in range(n):
                while r < n and (have < 5 or cons < m):
                    ch = word[r]
                    if ch in idx:
                        v = idx[ch]
                        if cnt[v] == 0:
                            have += 1
                        cnt[v] += 1
                    else:
                        cons += 1
                    r += 1
                if have == 5 and cons >= m:
                    res += n - r + 1
                else:
                    break
                ch = word[l]
                if ch in idx:
                    v = idx[ch]
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        have -= 1
                else:
                    cons -= 1
            return res

        return at_least(k) - at_least(k + 1)
