class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        last = [-1] * 26        # most recent index of each letter
        prev = [0] * n

        # pass 1: previous occurrence of each position
        for i, ch in enumerate(s):
            c = ord(ch) - 65
            prev[i] = last[c]
            last[c] = i

        # pass 2: next occurrence, accumulate contributions
        nxt = [n] * 26
        total = 0
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - 65
            total += (i - prev[i]) * (nxt[c] - i)
            nxt[c] = i

        return total
