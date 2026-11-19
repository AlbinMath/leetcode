from typing import List

class Solution:
    def canRemoveAll(self, types: List[int], colors: List[int], groupSize: List[int]) -> bool:
        stk = []  # list of [type, color, count]
        
        for t, c in zip(types, colors):
            if stk and stk[-1][0] == t and stk[-1][1] == c:
                stk[-1][2] += 1
            else:
                stk.append([t, c, 1])
                
            if stk[-1][2] == groupSize[t]:
                stk.pop()
                
        return not stk
