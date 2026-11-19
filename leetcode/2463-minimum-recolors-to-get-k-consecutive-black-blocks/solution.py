class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = blocks[:k].count('W')
        min_ops = white_count
        
        for i in range(k, len(blocks)):
            white_count += (blocks[i] == 'W') - (blocks[i - k] == 'W')
            if white_count < min_ops:
                min_ops = white_count
                if min_ops == 0:
                    return 0
                    
        return min_ops
