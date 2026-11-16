class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can(s: str, pos: int, remaining: int) -> bool:
            if pos == len(s):
                return remaining == 0
            val = 0
            for j in range(pos, len(s)):
                val = val * 10 + int(s[j])
                if val > remaining:
                    break  # pieces only grow as we extend, so stop
                if can(s, j + 1, remaining - val):
                    return True
            return False

        total = 0
        for i in range(1, n + 1):
            sq = i * i
            if can(str(sq), 0, i):
                total += sq
        return total
