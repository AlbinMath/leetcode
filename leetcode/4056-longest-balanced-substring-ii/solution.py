class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0

        # Case 1: single repeated letter
        run = 0
        for i in range(n):
            run = run + 1 if i and s[i] == s[i - 1] else 1
            res = max(res, run)

        # Case 2: exactly two letters, third letter excluded
        for x, y, z in (('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'c', 'a')):
            first = {0: -1}
            diff = 0
            for i, ch in enumerate(s):
                if ch == z:
                    first = {0: i}
                    diff = 0
                    continue
                diff += 1 if ch == x else -1
                if diff in first:
                    res = max(res, i - first[diff])
                else:
                    first[diff] = i

        # Case 3: all three letters equal
        first = {(0, 0): -1}
        a = b = c = 0
        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            key = (a - b, b - c)
            if key in first:
                res = max(res, i - first[key])
            else:
                first[key] = i

        return res
