class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = set()
        for b in bulbs:
            on ^= {b}
        return sorted(on)
