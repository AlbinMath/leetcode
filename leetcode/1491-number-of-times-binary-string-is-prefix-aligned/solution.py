class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        max_flipped = 0
        aligned_count = 0
        
        for step, pos in enumerate(flips, start=1):
            if pos > max_flipped:
                max_flipped = pos
            if max_flipped == step:
                aligned_count += 1
                
        return aligned_count
