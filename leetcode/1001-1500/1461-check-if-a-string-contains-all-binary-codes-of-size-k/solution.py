class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        if len(s) - k + 1 < need:
            return False
        mask = need - 1
        seen = [False] * need
        count = 0
        h = 0
        for i, ch in enumerate(s):
            h = ((h << 1) | (ord(ch) - 48)) & mask
            if i >= k - 1 and not seen[h]:
                seen[h] = True
                count += 1
                if count == need:
                    return True
        return False
