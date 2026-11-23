class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cur = arr[0]
        wins = 0

        for x in arr[1:]:
            if cur > x:
                wins += 1
            else:
                cur = x
                wins = 1
            if wins == k:
                return cur

        return cur
