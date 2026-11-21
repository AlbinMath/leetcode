class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if len(start) != len(result):
            return False

        n = len(start)
        i = j = 0

        while i < n or j < n:
            # skip X in both strings
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1

            # one string ran out of pieces before the other
            if i == n or j == n:
                return i == n and j == n

            if start[i] != result[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True
