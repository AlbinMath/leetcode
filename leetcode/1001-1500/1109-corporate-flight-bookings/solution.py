class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        res = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            res[i] = cur
        return res
