class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_pal(s: str, i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def check(x: str, y: str) -> bool:
            # prefix from x, suffix from y
            i, j = 0, len(x) - 1
            while i < j and x[i] == y[j]:
                i += 1
                j -= 1
            # core [i..j] must be a palindrome in x or in y
            return is_pal(x, i, j) or is_pal(y, i, j)

        return check(a, b) or check(b, a)
