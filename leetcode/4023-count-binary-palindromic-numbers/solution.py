class Solution(object):
    def countBinaryPalindromes(self, n):
        if n == 0:
            return 1
        B = n.bit_length()
        total = 1  # the number 0

        # all palindromes with fewer bits than n
        for L in range(1, B):
            total += 1 << ((L + 1) // 2 - 1)

        half = (B + 1) // 2

        def build(h):
            s = bin(h)[2:]
            tail = s[::-1] if B % 2 == 0 else s[:-1][::-1]
            return int(s + tail, 2)

        lo, hi = 1 << (half - 1), (1 << half) - 1
        # find the largest h with build(h) <= n
        ans = lo - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if build(mid) <= n:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        total += ans - (1 << (half - 1)) + 1
        return total
