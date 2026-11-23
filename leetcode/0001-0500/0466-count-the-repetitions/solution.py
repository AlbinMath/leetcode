class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        seen = {}          # j -> (i, count) at the start of copy i
        j = 0              # position in s2
        count = 0          # completed s2 copies so far
        i = 0
        extra = 0          # completions gained by skipped cycles
        while i < n1:
            if j in seen and extra == 0:
                pi, pc = seen[j]
                cycle_len = i - pi
                cycle_gain = count - pc
                skips = (n1 - i) // cycle_len
                i += skips * cycle_len
                extra = skips * cycle_gain
                if i >= n1:
                    break
            else:
                seen.setdefault(j, (i, count))
            for c in s1:
                if c == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        count += 1
            i += 1
        return (count + extra) // n2
