from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        total_rabbits = 0
        
        for ans, count in counts.items():
            group_size = ans + 1
            num_groups = (count + ans) // group_size
            total_rabbits += num_groups * group_size
            
        return total_rabbits
