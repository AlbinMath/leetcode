class Solution:

    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        import heapq

        n = len(nums)

        # -------------------------------------------------
        # Segment Tree
        # -------------------------------------------------

        size = 1
        while size < n:
            size <<= 1

        INF = 10**18

        segMax = [-INF] * (2 * size)
        segMin = [INF] * (2 * size)

        # Build leaves
        for i in range(n):
            segMax[size + i] = nums[i]
            segMin[size + i] = nums[i]

        # Build tree
        for i in range(size - 1, 0, -1):
            segMax[i] = max(segMax[i << 1], segMax[i << 1 | 1])
            segMin[i] = min(segMin[i << 1], segMin[i << 1 | 1])

        def getValue(l, r):
            """Return max(nums[l:r+1]) - min(nums[l:r+1])."""

            if l > r:
                return 0

            l += size
            r += size

            mx = -INF
            mn = INF

            while l <= r:

                if l & 1:
                    mx = max(mx, segMax[l])
                    mn = min(mn, segMin[l])
                    l += 1

                if not (r & 1):
                    mx = max(mx, segMax[r])
                    mn = min(mn, segMin[r])
                    r -= 1

                l >>= 1
                r >>= 1

            return mx - mn

        # -------------------------------------------------
        # Max heap
        #
        # Python has a min heap, so store -value.
        #
        # Initially, for every l, choose [l, n-1].
        # This is the largest value for that l.
        # -------------------------------------------------

        heap = []

        for l in range(n):
            value = getValue(l, n - 1)
            heapq.heappush(heap, (-value, l, n - 1))

        answer = 0

        # Extract the k largest subarray values.
        for _ in range(k):

            negValue, l, r = heapq.heappop(heap)

            value = -negValue
            answer += value

            # Move to the next smaller subarray
            # for the same left endpoint.
            if r > l:
                nr = r - 1
                nextValue = getValue(l, nr)

                heapq.heappush(
                    heap,
                    (-nextValue, l, nr)
                )

        return answer
