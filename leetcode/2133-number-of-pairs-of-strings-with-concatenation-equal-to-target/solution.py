from collections import Counter

class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        freq = Counter(nums)
        pairs = 0
        target_len = len(target)
        
        for prefix, count in freq.items():
            if len(prefix) < target_len and target.startswith(prefix):
                suffix = target[len(prefix):]
                if suffix in freq:
                    if prefix == suffix:
                        pairs += count * (count - 1)
                    else:
                        pairs += count * freq[suffix]
                        
        return pairs
