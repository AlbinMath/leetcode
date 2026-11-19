from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        type1 = type2 = -1
        last_streak = 0
        curr_len = max_len = 0
        
        for fruit in fruits:
            if fruit == type1 or fruit == type2:
                curr_len += 1
            else:
                curr_len = last_streak + 1
                
            if fruit == type2:
                last_streak += 1
            else:
                type1, type2 = type2, fruit
                last_streak = 1
                
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len
