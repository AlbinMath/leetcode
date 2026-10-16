class Solution:
    def findAnagrams(self, s, p):
        from collections import Counter
        a, b, res = Counter(p), Counter(), []
        for i, c in enumerate(s):
            b[c] += 1
            if i >= len(p):
                b[s[i-len(p)]] -= 1
                if b[s[i-len(p)]] == 0:
                    del b[s[i-len(p)]]
            if b == a:
                res.append(i-len(p)+1)
        return res
