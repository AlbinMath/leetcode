class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 1
        cur = 0
        for ch in s:
            d = int(ch)
            if d > k:
                return -1
            if cur * 10 + d <= k:
                cur = cur * 10 + d
            else:
                count += 1
                cur = d
        return count
