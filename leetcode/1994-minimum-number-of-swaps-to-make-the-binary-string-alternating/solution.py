class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones

        if abs(ones - zeros) > 1:
            return -1

        # mismatches against the target that starts with '0': 0101...
        mis0 = sum(1 for i, ch in enumerate(s) if ch != str(i % 2))
        # mismatches against the target that starts with '1': 1010...
        mis1 = n - mis0

        if ones > zeros:
            return mis1 // 2   # '1' must be at even indices
        if zeros > ones:
            return mis0 // 2   # '0' must be at even indices
        return min(mis0, mis1) // 2
