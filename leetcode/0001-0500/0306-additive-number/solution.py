class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(a: str) -> bool:
            return a == "0" or a[0] != "0"

        for i in range(1, n):
            a = num[:i]
            if not valid(a):
                break  # any longer first number also has the leading zero
            for j in range(1, n - i):
                b = num[i:i + j]
                if not valid(b):
                    break  # any longer second number also has the leading zero
                if max(i, j) > n - i - j:
                    continue

                x, y = int(a), int(b)
                pos = i + j
                while pos < n:
                    s = str(x + y)
                    if not num.startswith(s, pos):
                        break
                    pos += len(s)
                    x, y = y, x + y
                if pos == n:
                    return True
        return False
