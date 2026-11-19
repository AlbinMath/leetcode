from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        best_prefix = [0] * (n + 1)
        
        left = 0
        max_prizes = 0
        
        for right, pos in enumerate(prizePositions):
            while pos - prizePositions[left] > k:
                left += 1
                
            curr_win = right - left + 1
            if curr_win + best_prefix[left] > max_prizes:
                max_prizes = curr_win + best_prefix[left]
                
            best_prefix[right + 1] = max(best_prefix[right], curr_win)
            
        return max_prizes
