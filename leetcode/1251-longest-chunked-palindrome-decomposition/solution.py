class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        res = 0
        l, r = 0, n          # current middle is text[l:r]
        while l < r:
            found = False
            for length in range(1, (r - l) // 2 + 1):
                if text[l:l + length] == text[r - length:r]:
                    res += 2
                    l += length
                    r -= length
                    found = True
                    break
            if not found:
                res += 1     # the whole middle is one chunk
                break
        return res
