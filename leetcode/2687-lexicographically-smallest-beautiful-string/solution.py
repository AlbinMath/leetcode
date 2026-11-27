class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        a = [ord(c) - 97 for c in s]

        def ok(i: int, c: int) -> bool:
            if i >= 1 and a[i - 1] == c:
                return False
            if i >= 2 and a[i - 2] == c:
                return False
            return True

        for i in range(n - 1, -1, -1):
            for c in range(a[i] + 1, k):
                if ok(i, c):
                    a[i] = c
                    # fill the suffix greedily with the smallest valid letters
                    for j in range(i + 1, n):
                        for d in range(3):
                            if ok(j, d):
                                a[j] = d
                                break
                    return ''.join(chr(x + 97) for x in a)
        return ""
