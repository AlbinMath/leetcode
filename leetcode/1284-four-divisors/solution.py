from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            divs = set()
            i = 1
            while i * i <= x:
                if x % i == 0:
                    divs.add(i)
                    divs.add(x // i)
                    if len(divs) > 4:
                        break
                i += 1
            if len(divs) == 4:
                total += sum(divs)
        return total
