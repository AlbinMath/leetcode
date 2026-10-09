
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        perm = []

        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1

        perm.append(low)

        return perm

