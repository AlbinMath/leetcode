class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = {}
        
        for winner, loser in matches:
            losses.setdefault(winner, 0)
            losses[loser] = losses.get(loser, 0) + 1
            
        zero_losses = [player for player, count in losses.items() if count == 0]
        one_loss = [player for player, count in losses.items() if count == 1]
        
        return [sorted(zero_losses), sorted(one_loss)]
