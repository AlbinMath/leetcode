class Solution(object):
    def superpalindromesInRange(self, left, right):
        L = int(left)
        R = int(right)
        MAGIC = 100000  # Generates palindrome roots up to 9 digits (< 10^9)
        count = 0

        # Check odd-length palindrome roots (e.g., 123 -> 12321)
        for k in range(1, MAGIC):
            s = str(k)
            p = int(s + s[-2::-1])
            sq = p * p
            if sq > R:
                break
            if sq >= L and str(sq) == str(sq)[::-1]:
                count += 1

        # Check even-length palindrome roots (e.g., 123 -> 123321)
        for k in range(1, MAGIC):
            s = str(k)
            p = int(s + s[::-1])
            sq = p * p
            if sq > R:
                break
            if sq >= L and str(sq) == str(sq)[::-1]:
                count += 1

        return count
