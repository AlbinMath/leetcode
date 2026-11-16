class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        if 8 <= n <= 11:
            return 11  # the only even-length prime palindrome

        for root in range(1, 10 ** 5):
            s = str(root)
            p = int(s + s[-2::-1])  # odd-length palindrome, middle digit not repeated
            if p >= n and is_prime(p):
                return p
        return -1
