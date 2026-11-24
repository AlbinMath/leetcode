class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for a, b in zip(s, t):
            d = (ord(b) - ord(a)) % 26
            if d == 0:
                continue
            # the (count[d]+1)-th index needing shift d uses move d + 26 * count[d]
            if d + 26 * count[d] > k:
                return False
            count[d] += 1

        return True
