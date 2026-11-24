from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def min_steps(left_pos: int, right_pos: int) -> int:
            return (right_pos - left_pos) + min(abs(startPos - left_pos), abs(startPos - right_pos))
        
        left = 0
        curr_fruits = 0
        max_fruits = 0
        
        for right, (pos, amount) in enumerate(fruits):
            curr_fruits += amount
            while left <= right and min_steps(fruits[left][0], pos) > k:
                curr_fruits -= fruits[left][1]
                left += 1
            if curr_fruits > max_fruits:
                max_fruits = curr_fruits
                
        return max_fruits
