class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        landed = []  
        ans = []
        max_height = 0
        
        for left, size in positions:
            right = left + size
            base_height = 0
            
            for prev_l, prev_r, prev_h in landed:
                if left < prev_r and prev_l < right:
                    if prev_h > base_height:
                        base_height = prev_h
                        
            current_height = base_height + size
            landed.append((left, right, current_height))
            
            max_height = max(max_height, current_height)
            ans.append(max_height)
            
        return ans
