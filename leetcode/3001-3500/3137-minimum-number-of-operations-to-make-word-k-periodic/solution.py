from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        block_counts = Counter(word[i : i + k] for i in range(0, n, k))
        
        return (n // k) - max(block_counts.values())
