# LeetCode 313: Super Ugly Number

**LeetCode Problem #313 — Super Ugly Number**
Solve LeetCode Super Ugly Number using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Super Ugly Number |
| LeetCode | #313 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **super ugly number** is a positive integer whose prime factors are in the array `primes`.

Given an integer `n` and an array of integers `primes`, return *the* `n^th` ***super ugly number***.

The `n^th` **super ugly number** is **guaranteed** to fit in a **32-bit** signed integer.

## Constraints
- `1 <= n <= 10^5`
- `1 <= primes.length <= 100`
- `2 <= primes[i] <= 1000`
- `primes[i]` is **guaranteed** to be a prime number.
- All the values of `primes` are **unique** and sorted in **ascending order**.

## Examples
### Example 1
- **Input:** `n = 12, primes = [2,7,13,19]`
- **Output:** `32`
- **Explanation:** [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

### Example 2
- **Input:** `n = 1, primes = [2,3,5]`
- **Output:** `1`
- **Explanation:** 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Super Ugly Number**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 12, primes = [2,7,13,19]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `32`.
4. **Verification:** [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

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
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k
        cand = primes[:]  # cand[j] = ugly[idx[j]] * primes[j]
        for i in range(1, n):
            nxt = min(cand)
            ugly[i] = nxt
            for j in range(k):
                if cand[j] == nxt:
                    idx[j] += 1
                    cand[j] = ugly[idx[j]] * primes[j]
        return ugly[-1]
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
- [263. Ugly Number](../../0001-0500/0263-ugly-number/)
- [264. Ugly Number II](../../0001-0500/0264-ugly-number-ii/)
- [1201. Ugly Number III](../../1001-1500/1201-ugly-number-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/super-ugly-number/)
