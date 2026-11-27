from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int,
                         energy: List[int], experience: List[int]) -> int:
        hours = max(0, sum(energy) + 1 - initialEnergy)
        exp = initialExperience
        for e in experience:
            if exp <= e:
                need = e + 1 - exp
                hours += need
                exp += need
            exp += e
        return hours
