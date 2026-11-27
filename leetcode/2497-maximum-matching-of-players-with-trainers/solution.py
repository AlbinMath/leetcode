from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        for t in trainers:
            if i < len(players) and players[i] <= t:
                i += 1
        return i
