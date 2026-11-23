import heapq
from collections import Counter

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        freq = Counter(ch for ch in s if ch != '?')
        q_count = s.count('?')
        
        heap = [(freq[chr(ord('a') + i)], chr(ord('a') + i)) for i in range(26)]
        heapq.heapify(heap)
        
        replacements = []
        for _ in range(q_count):
            count, ch = heapq.heappop(heap)
            replacements.append(ch)
            heapq.heappush(heap, (count + 1, ch))
            
        replacements.sort()
        
        res = list(s)
        idx = 0
        for i, ch in enumerate(res):
            if ch == '?':
                res[i] = replacements[idx]
                idx += 1
                
        return "".join(res)
