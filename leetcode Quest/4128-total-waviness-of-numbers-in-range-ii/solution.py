class Solution:

    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n):
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # State:
            # (tight, started, prevPrev, prev)
            #
            # value = (number of ways, total waviness)
            #
            # prevPrev = -1 means we don't have two previous
            # digits yet.
            dp = {
                (True, False, -1, -1): (1, 0)
            }

            for pos in range(m):
                ndp = {}

                for (tight, started, pp, p), (ways, total) in dp.items():

                    limit = digits[pos] if tight else 9

                    for d in range(limit + 1):

                        ntight = tight and (d == limit)

                        # Still skipping leading zeros
                        if not started and d == 0:
                            key = (ntight, False, -1, -1)

                            oldWays, oldTotal = ndp.get(key, (0, 0))
                            ndp[key] = (
                                oldWays + ways,
                                oldTotal + total
                            )
                            continue

                        # First real digit
                        if not started:
                            key = (ntight, True, -1, d)

                            oldWays, oldTotal = ndp.get(key, (0, 0))
                            ndp[key] = (
                                oldWays + ways,
                                oldTotal + total
                            )
                            continue

                        # We have only one previous digit.
                        if pp == -1:
                            key = (ntight, True, p, d)

                            oldWays, oldTotal = ndp.get(key, (0, 0))
                            ndp[key] = (
                                oldWays + ways,
                                oldTotal + total
                            )
                            continue

                        # We now have:
                        #
                        # pp, p, d
                        #
                        # p is a peak if p > pp and p > d
                        # p is a valley if p < pp and p < d

                        add = 0

                        if (p > pp and p > d) or \
                           (p < pp and p < d):
                            add = 1

                        key = (ntight, True, p, d)

                        oldWays, oldTotal = ndp.get(key, (0, 0))

                        ndp[key] = (
                            oldWays + ways,
                            oldTotal + total + ways * add
                        )

                dp = ndp

            # Sum waviness over all numbers <= n.
            answer = 0

            for (tight, started, pp, p), (ways, total) in dp.items():
                answer += total

            return answer

        return solve(num2) - solve(num1 - 1)
