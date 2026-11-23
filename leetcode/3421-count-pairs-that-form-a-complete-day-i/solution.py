class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        rem_counts = [0] * 24
        pairs = 0
        
        for h in hours:
            rem = h % 24
            complement = (24 - rem) % 24
            pairs += rem_counts[complement]
            rem_counts[rem] += 1
            
        return pairs
