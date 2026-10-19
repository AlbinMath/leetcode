class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                small.append(i)
            i += 1

        # k falls among the small factors
        if k <= len(small):
            return small[k - 1]

        # otherwise it is among the large partners, in reverse order
        large = [n // d for d in reversed(small)]
        if small and small[-1] * small[-1] == n:
            large = large[1:]            # drop the duplicated square root
        k -= len(small)
        return large[k - 1] if k <= len(large) else -1
