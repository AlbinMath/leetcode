# LeetCode 1175: Prime Arrangements

**LeetCode Problem #1175 — Prime Arrangements**
Solve LeetCode Prime Arrangements using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Prime Arrangements |
| LeetCode | #1175 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Return the number of permutations of 1 to `n` so that prime numbers are at prime indices (1-indexed.)

*(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)*

Since the answer may be large, return the answer **modulo `10^9 + 7`**.

## Constraints
- `1 <= n <= 100`

## Examples
### Example 1
- **Input:** `n = 5`
- **Output:** `12`
- **Explanation:** For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

### Example 2
- **Input:** `n = 100`
- **Output:** `682289015`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Prime Arrangements**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3426. Manhattan Distances of All Arrangements of Pieces](../../3001-3500/3426-manhattan-distances-of-all-arrangements-of-pieces/)
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)
- [866. Prime Palindrome](../../0501-1000/0866-prime-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/prime-arrangements/)
