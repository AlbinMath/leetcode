class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        moves = 0
        nxt = 0  # smallest value the next element may take
        for x in nums:
            if x < nxt:
                moves += nxt - x
                nxt += 1
            else:
                nxt = x + 1
        return moves
