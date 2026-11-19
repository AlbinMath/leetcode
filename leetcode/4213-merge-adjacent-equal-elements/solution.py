from typing import List

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stk = []
        
        for x in nums:
            curr = x
            while stk and stk[-1] == curr:
                curr += stk.pop()
            stk.append(curr)
            
        return stk
