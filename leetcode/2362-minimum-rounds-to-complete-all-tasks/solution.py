from collections import Counter

class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        freq = Counter(tasks)
        total_rounds = 0
        
        for count in freq.values():
            if count == 1:
                return -1
            total_rounds += (count + 2) // 3
            
        return total_rounds
