class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        base = minutesToTest // minutesToDie + 1
        pigs, cap = 0, 1
        while cap < buckets:
            cap *= base
            pigs += 1
        return pigs
