from typing import List

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        
        right = 0
        full_cover = 0
        max_tiles = 0
        
        for left in range(n):
            end_pos = tiles[left][0] + carpetLen - 1
            
            while right < n and tiles[right][1] <= end_pos:
                full_cover += tiles[right][1] - tiles[right][0] + 1
                right += 1
                
            if right < n and tiles[right][0] <= end_pos:
                partial = end_pos - tiles[right][0] + 1
                if full_cover + partial > max_tiles:
                    max_tiles = full_cover + partial
            elif full_cover > max_tiles:
                max_tiles = full_cover
                
            if max_tiles == carpetLen:
                return carpetLen
                
            if left < right:
                full_cover -= tiles[left][1] - tiles[left][0] + 1
            else:
                right = left + 1
                
        return max_tiles
