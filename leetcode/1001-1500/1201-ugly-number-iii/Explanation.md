# LeetCode 1201: Ugly Number III

**LeetCode Problem #1201 — Ugly Number III**
Solve LeetCode Ugly Number III using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Ugly Number III |
| LeetCode | #1201 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
An **ugly number** is a positive integer that is divisible by `a`, `b`, or `c`.

Given four integers `n`, `a`, `b`, and `c`, return the `n^th` **ugly number**.

## Constraints
- `1 <= n, a, b, c <= 10^9`
- `1 <= a * b * c <= 10^18`
- It is guaranteed that the result will be in range `[1, 2 * 10^9]`.

## Examples
### Example 1
- **Input:** `n = 3, a = 2, b = 3, c = 5`
- **Output:** `4`
- **Explanation:** The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3^rd is 4.

### Example 2
- **Input:** `n = 4, a = 2, b = 3, c = 4`
- **Output:** `6`
- **Explanation:** The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4^th is 6.

### Example 3
- **Input:** `n = 5, a = 2, b = 11, c = 13`
- **Output:** `10`
- **Explanation:** The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5^th is 10.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Ugly Number III**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, a = 2, b = 3, c = 5`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3^rd is 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a // gcd(a, b) * b
        ac = a // gcd(a, c) * c
        bc = b // gcd(b, c) * c
        abc = ab // gcd(ab, c) * c

        def count(x):
            return (x // a + x // b + x // c
                    - x // ab - x // ac - x // bc
                    + x // abc)

        lo, hi = 1, 2 * 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

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
- [313. Super Ugly Number](../../0001-0500/0313-super-ugly-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/ugly-number-iii/)
