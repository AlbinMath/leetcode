class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = 'L' + dominoes + 'R'
        res = []
        prev = 0  # index of the previous force character in s

        for i in range(1, len(s)):
            if s[i] == '.':
                continue

            gap = i - prev - 1
            if prev > 0:
                res.append(s[prev])  # emit the force character itself

            if s[prev] == s[i]:
                res.append(s[i] * gap)             # L..L or R..R
            elif s[prev] == 'L' and s[i] == 'R':
                res.append('.' * gap)              # pushed apart
            else:                                  # R..L
                res.append('R' * (gap // 2))
                res.append('.' * (gap % 2))
                res.append('L' * (gap // 2))

            prev = i

        return ''.join(res)
