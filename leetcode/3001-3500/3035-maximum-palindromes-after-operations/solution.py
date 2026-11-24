from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        freq = Counter(ch for word in words for ch in word)
        total_pairs = sum(count // 2 for count in freq.values())
        
        lengths = sorted(len(word) for word in words)
        palindromes = 0
        
        for length in lengths:
            needed_pairs = length // 2
            if total_pairs >= needed_pairs:
                total_pairs -= needed_pairs
                palindromes += 1
            else:
                break
                
        return palindromes
