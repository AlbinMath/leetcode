class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        steps = 0
        for i, p in enumerate(plants):
            if water < p:
                steps += 2 * i + 1
                water = capacity
            else:
                steps += 1
            water -= p
        return steps
