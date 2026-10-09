class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        primes = 0

        for num in range(2, n + 1):
            is_prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes += 1

        non_primes = n - primes

        def factorial(x):
            result = 1
            for i in range(2, x + 1):
                result = (result * i) % MOD
            return result

        return (factorial(primes) * factorial(non_primes)) % MOD
