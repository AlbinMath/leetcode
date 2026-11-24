from collections import Counter
from itertools import groupby

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        total = Counter(text)
        runs = [(ch, sum(1 for _ in grp)) for ch, grp in groupby(text)]
        
        ans = 0
        for i, (ch, length) in enumerate(runs):
            ans = max(ans, min(length + 1, total[ch]))
            
            if 0 < i < len(runs) - 1 and length == 1 and runs[i - 1][0] == runs[i + 1][0]:
                adj_ch = runs[i - 1][0]
                merged = runs[i - 1][1] + runs[i + 1][1] + 1
                ans = max(ans, min(merged, total[adj_ch]))
                
        return ans
