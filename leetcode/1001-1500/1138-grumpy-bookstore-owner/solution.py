from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base_satisfied = 0
        curr_extra = 0
        max_extra = 0
        
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g == 0:
                base_satisfied += c
            else:
                curr_extra += c
                
            if i >= minutes and grumpy[i - minutes] == 1:
                curr_extra -= customers[i - minutes]
                
            if curr_extra > max_extra:
                max_extra = curr_extra
                
        return base_satisfied + max_extra
