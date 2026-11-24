from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        curr_score = sum(cardPoints[:k])
        max_score = curr_score
        
        for step in range(1, k + 1):
            curr_score += cardPoints[n - step] - cardPoints[k - step]
            if curr_score > max_score:
                max_score = curr_score
                
        return max_score
