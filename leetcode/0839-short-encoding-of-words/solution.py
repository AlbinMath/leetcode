from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        keep = set(words)
        for w in words:
            for i in range(1, len(w)):
                keep.discard(w[i:])
        return sum(len(w) + 1 for w in keep)
