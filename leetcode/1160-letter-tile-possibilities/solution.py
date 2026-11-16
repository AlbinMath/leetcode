from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)

        def dfs() -> int:
            total = 0
            for ch in cnt:
                if cnt[ch] == 0:
                    continue
                cnt[ch] -= 1
                total += 1 + dfs()  # 1 for the sequence ending here
                cnt[ch] += 1
            return total

        return dfs()
