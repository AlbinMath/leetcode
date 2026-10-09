from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        give = 1
        i = 0

        while candies > 0:
            amount = min(give, candies)
            result[i % num_people] += amount
            candies -= amount
            give += 1
            i += 1

        return result
