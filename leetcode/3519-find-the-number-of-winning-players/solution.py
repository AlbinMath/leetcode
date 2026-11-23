class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        counts = [[0] * 11 for _ in range(n)]
        winners = set()
        
        for player, color in pick:
            counts[player][color] += 1
            if counts[player][color] > player:
                winners.add(player)
                
        return len(winners)
