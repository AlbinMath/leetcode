class Solution(object):
    def countPairs(self, coordinates, k):
        seen = {}
        ans = 0
        for x, y in coordinates:
            for a in range(k + 1):
                key = (x ^ a, y ^ (k - a))
                ans += seen.get(key, 0)
            p = (x, y)
            seen[p] = seen.get(p, 0) + 1
        return ans
