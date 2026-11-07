class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1: 0}

        def power(x):
            path = []
            while x not in cache:
                path.append(x)
                x = x // 2 if x % 2 == 0 else 3 * x + 1
            steps = cache[x]
            for v in reversed(path):
                steps += 1
                cache[v] = steps
            return cache[path[0]] if path else steps

        nums = sorted(range(lo, hi + 1), key=lambda v: (power(v), v))
        return nums[k - 1]
