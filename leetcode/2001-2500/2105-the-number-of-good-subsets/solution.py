
class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        freq = [0] * 31

        for num in nums:
            freq[num] += 1

        # dp[mask] = number of subsets with this prime-factor mask
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num in range(2, 31):
            if freq[num] == 0:
                continue

            mask = 0
            valid = True

            for i, prime in enumerate(primes):
                if num % (prime * prime) == 0:
                    valid = False
                    break

                if num % prime == 0:
                    mask |= 1 << i

            if not valid:
                continue

            # Descending masks prevent using the same number twice
            for state in range((1 << 10) - 1, -1, -1):
                if state & mask == 0:
                    new_state = state | mask
                    dp[new_state] = (
                        dp[new_state] + dp[state] * freq[num]
                    ) % MOD

        # Exclude the empty subset (mask = 0)
        answer = sum(dp[1:]) % MOD

        # Each good subset can include any subset of the 1s
        answer = answer * pow(2, freq[1], MOD) % MOD

        return answer

