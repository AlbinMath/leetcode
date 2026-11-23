class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        cur = 0
        total = 0
        for f in requests:
            total += abs(f - cur)
            cur = f
        return total
