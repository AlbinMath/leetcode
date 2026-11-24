class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        need = [0] * 123          # indexed directly by byte value
        for b in word2.encode():
            need[b] += 1
        missing = sum(1 for x in need if x)

        cnt = [0] * 123
        data = word1.encode()     # bytes: iterating/indexing gives ints
        ans = 0
        r = 0
        for l in range(n):
            while missing and r < n:
                c = data[r]
                cnt[c] += 1
                if cnt[c] == need[c]:
                    missing -= 1
                r += 1
            if missing:
                break             # r hit n and the window can't become valid; later l can't either
            ans += n - r + 1
            c = data[l]
            if cnt[c] == need[c]:
                missing += 1
            cnt[c] -= 1
        return ans
