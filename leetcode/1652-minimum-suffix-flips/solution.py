class Solution:
    def minFlips(self, target: str) -> int:
        prev = '0'
        flips = 0

        for ch in target:
            if ch != prev:
                flips += 1
                prev = ch

        return flips
