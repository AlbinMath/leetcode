class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        flowers = sorted(min(f, target) for f in flowers)
        n = len(flowers)

        # Gardens already complete don't need any new flowers
        already_full = 0
        while flowers and flowers[-1] == target:
            flowers.pop()
            already_full += 1

        m = len(flowers)
        if m == 0:
            return n * full

        # cost[i] = flowers needed to raise flowers[0..i] all up to flowers[i]
        cost = [0] * m
        for i in range(1, m):
            cost[i] = cost[i - 1] + i * (flowers[i] - flowers[i - 1])

        ans = 0
        rem = newFlowers
        j = m - 1

        # Try completing the k largest incomplete gardens (from right to left)
        for k in range(m + 1):
            if k > 0:
                rem -= target - flowers[m - k]
                if rem < 0:
                    break

            if k == m:
                ans = max(ans, (already_full + m) * full)
                break

            while j >= m - k or cost[j] > rem:
                j -= 1

            min_incomplete = min(target - 1, flowers[j] + (rem - cost[j]) // (j + 1))
            ans = max(ans, (already_full + k) * full + min_incomplete * partial)

        return ans
