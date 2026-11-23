class Solution:

    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        # Maximum coordinate that can appear.
        max_x = 0

        for q in queries:
            max_x = max(max_x, q[1])

        size = 4 * (max_x + 2)

        # Segment tree arrays.
        #
        # first[node] = first obstacle in this segment
        # last[node]  = last obstacle in this segment
        # gap[node]   = maximum gap between obstacles
        #
        # -1 means there is no obstacle.
        first = [-1] * size
        last = [-1] * size
        gap = [0] * size

        def pull(node):
            left = node * 2
            right = left + 1

            # Only left child has obstacles
            if first[right] == -1:
                first[node] = first[left]
                last[node] = last[left]
                gap[node] = gap[left]
                return

            # Only right child has obstacles
            if first[left] == -1:
                first[node] = first[right]
                last[node] = last[right]
                gap[node] = gap[right]
                return

            # Both sides contain obstacles.
            first[node] = first[left]
            last[node] = last[right]

            gap[node] = max(
                gap[left],
                gap[right],
                first[right] - last[left]
            )

        def update(node, lo, hi, pos):
            if lo == hi:
                first[node] = pos
                last[node] = pos
                gap[node] = 0
                return

            mid = (lo + hi) // 2

            if pos <= mid:
                update(node * 2, lo, mid, pos)
            else:
                update(node * 2 + 1, mid + 1, hi, pos)

            pull(node)

        def query(node, lo, hi, ql, qr):
            # No overlap
            if qr < lo or hi < ql:
                return (-1, -1, 0)

            # Complete overlap
            if ql <= lo and hi <= qr:
                return (
                    first[node],
                    last[node],
                    gap[node]
                )

            mid = (lo + hi) // 2

            lf, ll, lg = query(
                node * 2,
                lo,
                mid,
                ql,
                qr
            )

            rf, rl, rg = query(
                node * 2 + 1,
                mid + 1,
                hi,
                ql,
                qr
            )

            # Left empty
            if lf == -1:
                return (rf, rl, rg)

            # Right empty
            if rf == -1:
                return (lf, ll, lg)

            return (
                lf,
                rl,
                max(lg, rg, rf - ll)
            )

        answer = []

        for q in queries:

            # Type 1: add obstacle
            if q[0] == 1:
                x = q[1]
                update(1, 1, max_x, x)

            # Type 2: check block placement
            else:
                x = q[1]
                sz = q[2]

                # Obstacles only matter in [1, x].
                f, l, max_gap = query(
                    1,
                    1,
                    max_x,
                    1,
                    x
                )

                # No obstacle in [1, x].
                if f == -1:
                    answer.append(x >= sz)
                    continue

                # Gap from origin to first obstacle.
                max_gap = max(max_gap, f)

                # Gap from last obstacle to x.
                max_gap = max(max_gap, x - l)

                answer.append(max_gap >= sz)

        return answer
