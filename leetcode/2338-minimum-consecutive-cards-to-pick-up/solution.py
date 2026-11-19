from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}
        min_len = float('inf')
        
        for i, val in enumerate(cards):
            if val in last_seen:
                length = i - last_seen[val] + 1
                if length == 2:
                    return 2
                if length < min_len:
                    min_len = length
            last_seen[val] = i
            
        return -1 if min_len == float('inf') else min_len
