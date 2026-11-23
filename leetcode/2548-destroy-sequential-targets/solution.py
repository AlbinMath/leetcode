from collections import Counter

class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        rem_counts = Counter(num % space for num in nums)
        max_targets = max(rem_counts.values())
        
        return min(num for num in nums if rem_counts[num % space] == max_targets)
