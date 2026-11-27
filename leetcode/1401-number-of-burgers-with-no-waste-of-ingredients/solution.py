class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        if (
            tomatoSlices % 2 != 0
            or tomatoSlices < 2 * cheeseSlices
            or tomatoSlices > 4 * cheeseSlices
        ):
            return []
            
        jumbo = tomatoSlices // 2 - cheeseSlices
        small = cheeseSlices - jumbo
        return [jumbo, small]
