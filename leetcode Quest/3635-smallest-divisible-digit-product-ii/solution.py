class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """

        # Prime factorization of t
        need = [0, 0, 0, 0]  # 2, 3, 5, 7

        for i, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                need[i] += 1
                t //= p

        # Impossible: digit products only contain 2,3,5,7
        if t != 1:
            return "-1"

        # Factor contribution of digits 0...9
        factors = (
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        )

        # ---------------------------------------------------------
        # DP:
        # dp[a,b,c,d] = minimum number of digits required
        # to provide at least a 2s, b 3s, c 5s, d 7s.
        # ---------------------------------------------------------

        A = need[0] + 1
        B = need[1] + 1
        C = need[2] + 1
        D = need[3] + 1

        CD = C * D
        BCD = B * C * D

        size = A * BCD

        dp = bytearray([255]) * size
        dp[0] = 0

        def idx(a, b, c, d):
            return a * BCD + b * CD + c * D + d

        for a in range(A):
            for b in range(B):
                for c in range(C):
                    for d in range(D):

                        if a == 0 and b == 0 and c == 0 and d == 0:
                            continue

                        best = 255

                        for digit in range(2, 10):
                            f = factors[digit]

                            na = max(0, a - f[0])
                            nb = max(0, b - f[1])
                            nc = max(0, c - f[2])
                            nd = max(0, d - f[3])

                            value = dp[idx(na, nb, nc, nd)] + 1

                            if value < best:
                                best = value

                        dp[idx(a, b, c, d)] = best

        def min_digits(a, b, c, d):
            return dp[idx(a, b, c, d)]

        def subtract(req, digit):
            f = factors[digit]

            return (
                max(0, req[0] - f[0]),
                max(0, req[1] - f[1]),
                max(0, req[2] - f[2]),
                max(0, req[3] - f[3])
            )

        # ---------------------------------------------------------
        # Check if num itself is already valid
        # ---------------------------------------------------------

        cur = [0, 0, 0, 0]
        total_zero = 0

        for ch in num:
            digit = ord(ch) - 48

            if digit == 0:
                total_zero += 1
                continue

            f = factors[digit]

            for j in range(4):
                cur[j] = min(
                    need[j],
                    cur[j] + f[j]
                )

        if (
            total_zero == 0
            and cur[0] >= need[0]
            and cur[1] >= need[1]
            and cur[2] >= need[2]
            and cur[3] >= need[3]
        ):
            return num

        # ---------------------------------------------------------
        # Total factors in num
        # ---------------------------------------------------------

        total = [0, 0, 0, 0]

        for ch in num:
            digit = ord(ch) - 48

            if digit == 0:
                continue

            f = factors[digit]

            total[0] += f[0]
            total[1] += f[1]
            total[2] += f[2]
            total[3] += f[3]

        # ---------------------------------------------------------
        # Try to construct a valid number of the SAME length
        # ---------------------------------------------------------

        n = len(num)

        # prefix factors for [0, i)
        prefix = total[:]

        # Number of zeros in the suffix [i, n)
        suffix_zero = 0

        for i in range(n - 1, -1, -1):

            digit_at_i = ord(num[i]) - 48

            # Remove num[i] from prefix
            if digit_at_i == 0:
                suffix_zero += 1
            else:
                f = factors[digit_at_i]

                prefix[0] -= f[0]
                prefix[1] -= f[1]
                prefix[2] -= f[2]
                prefix[3] -= f[3]

            # Prefix [0, i) must not contain zero.
            prefix_zero = total_zero - suffix_zero

            if prefix_zero == 0:

                # Factors still required after the prefix
                req = (
                    max(0, need[0] - prefix[0]),
                    max(0, need[1] - prefix[1]),
                    max(0, need[2] - prefix[2]),
                    max(0, need[3] - prefix[3])
                )

                # Make current digit slightly larger
                for digit in range(digit_at_i + 1, 10):

                    nxt = subtract(req, digit)

                    remaining = n - i - 1

                    if min_digits(*nxt) <= remaining:

                        answer = num[:i] + str(digit)

                        # Build lexicographically smallest suffix
                        req = nxt

                        for pos in range(remaining):

                            left = remaining - pos - 1

                            for d in range(1, 10):

                                candidate = subtract(req, d)

                                if min_digits(*candidate) <= left:
                                    answer += str(d)
                                    req = candidate
                                    break

                        return answer

        # ---------------------------------------------------------
        # No answer with same length.
        # Find smallest valid longer number.
        # ---------------------------------------------------------

        length = min_digits(*need)

        if length <= n:
            length = n + 1

        answer = []
        req = tuple(need)

        for pos in range(length):

            remaining = length - pos - 1

            for digit in range(1, 10):

                nxt = subtract(req, digit)

                if min_digits(*nxt) <= remaining:
                    answer.append(str(digit))
                    req = nxt
                    break

        return "".join(answer)
