# LeetCode 1680: Concatenation of Consecutive Binary Numbers

**LeetCode Problem #1680 — Concatenation of Consecutive Binary Numbers**
Solve LeetCode Concatenation of Consecutive Binary Numbers using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Concatenation of Consecutive Binary Numbers |
| LeetCode | #1680 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *the **decimal value** of the binary string formed by concatenating the binary representations of *`1`* to *`n`* in order, **modulo ***`10^9 + 7`.

## Constraints
- `1 <= n <= 10^5`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `1`
- **Explanation:** "1" in binary corresponds to the decimal value 1.

### Example 2
- **Input:** `n = 3`
- **Output:** `27`
- **Explanation:** In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

### Example 3
- **Input:** `n = 12`
- **Output:** `505379714`
- **Explanation:** : The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 10^9 + 7, the result is 505379714.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Concatenation of Consecutive Binary Numbers**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** "1" in binary corresponds to the decimal value 1.

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
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0
        bits = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                bits += 1
            res = ((res << bits) | i) % MOD
        return res
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
- [1022. Sum of Root To Leaf Binary Numbers](../../1001-1500/1022-sum-of-root-to-leaf-binary-numbers/)
- [1689. Partitioning Into Minimum Number Of Deci-Binary Numbers](../../1501-2000/1689-partitioning-into-minimum-number-of-deci-binary-numbers/)
- [3309. Maximum Possible Number by Binary Concatenation](../../3001-3500/3309-maximum-possible-number-by-binary-concatenation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/)
