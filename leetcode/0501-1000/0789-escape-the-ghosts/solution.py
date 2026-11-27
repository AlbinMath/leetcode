class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        tx, ty = target
        player_dist = abs(tx) + abs(ty)
        
        for gx, gy in ghosts:
            ghost_dist = abs(gx - tx) + abs(gy - ty)
            if ghost_dist <= player_dist:
                return False
                
        return True
