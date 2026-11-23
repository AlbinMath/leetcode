from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        return ''.join(ch * c for ch, c in cnt.most_common())
