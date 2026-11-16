import math

class Solution(object):
    def bestCoordinate(self, towers, radius):
        max_x = max(t[0] for t in towers)
        max_y = max(t[1] for t in towers)
        r_sq = radius * radius
        
        best_quality = -1
        best_coord = [0, 0]
        
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                quality = 0
                for tx, ty, q in towers:
                    d_sq = (x - tx) ** 2 + (y - ty) ** 2
                    if d_sq <= r_sq:
                        quality += int(q / (1 + math.sqrt(d_sq)))
                
                if quality > best_quality:
                    best_quality = quality
                    best_coord = [x, y]
                    
        return best_coord
