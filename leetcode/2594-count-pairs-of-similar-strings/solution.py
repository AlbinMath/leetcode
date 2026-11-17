class Solution(object):
    def similarPairs(self, words):
        cnt = {}
        ans = 0
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - 97)
            c = cnt.get(m, 0)
            ans += c
            cnt[m] = c + 1
        return ans
