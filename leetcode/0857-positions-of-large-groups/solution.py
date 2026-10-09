
class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result = []
        n = len(s)
        i = 0

        while i < n:
            j = i

            # Find the end of the consecutive group
            while j < n and s[j] == s[i]:
                j += 1

            # A group is large if it contains at least 3 characters
            if j - i >= 3:
                result.append([i, j - 1])

            i = j

        return result

