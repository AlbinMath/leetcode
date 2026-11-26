from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        # Max possible sum is 2^20 + 2^20 = 2^21
        powers_of_two = [1 << i for i in range(22)]
        
        seen = defaultdict(int)
        total_meals = 0
        
        for x in deliciousness:
            for power in powers_of_two:
                target = power - x
                if target in seen:
                    total_meals = (total_meals + seen[target]) % MOD
            seen[x] += 1
            
        return total_meals
