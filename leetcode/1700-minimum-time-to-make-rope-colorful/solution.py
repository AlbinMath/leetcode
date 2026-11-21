class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        prev_max = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                total += min(prev_max, neededTime[i])
                prev_max = max(prev_max, neededTime[i])
            else:
                prev_max = neededTime[i]

        return total
